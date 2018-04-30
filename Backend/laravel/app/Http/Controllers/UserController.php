<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use Auth;
use Hash;
use App\Bot;
Use DB;


class UserController extends Controller
{

    public function getUser() {
        return Auth::user();
    }

    public function reset(Request $request) {
        $user_id = Auth::User()->id;                       
        $obj_user = User::find($user_id);
        if(strlen($request->input('email')) > 0) {    
            $obj_user->email = $request->input('email');
        }
        if(strlen($request->input('password')) > 0) {    
            $current_password = Auth::User()->password;       
            if(Hash::check($request->input('oldpass'), $current_password) AND $request->input('password') == $request->input('password_confirmation')) {           
                $obj_user->password = Hash::make($request->input('password'));
                $obj_user->save(); 
            }
        }
        $obj_user->save(); 
        return redirect()->route('account');
    }

    public function logout(Request $request) {
        Auth::logout();
        $request->session()->flush();
        $request->session()->regenerate();
        return redirect()->route('login');
    }

    public function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    public function checkPremium() {
        $user = Auth::User();
        if($user->premium == 0)
            return false;
        $date_now = date('Y-m-d');
        if(strtotime($date_now) > strtotime($user->expire_date)){
            $user->premium = 0;
            $user->save;
            return false;
        } else {
            return true;
        }
    }


    ##BITTREX
    public function update_api_bittrex(Request $request) {
        $user = Auth::user();
        $user->bit_api_secret = UserController::test_input($request['bit_api_secret']);
        $user->bit_api_key = UserController::test_input($request['bit_api_key']);
        $user->save();
        return redirect()->route('account');
    }

    public function bittrex_balance($currency) {
        $nonce = time();
        $user = Auth::user();
        ###############
        if($user->premium > 0 and strlen($user->bit_api_key) > 0 and strlen($user->bit_api_secret)) {
            $uri='https://bittrex.com/api/v1.1/account/getbalances?apikey='.$user->bit_api_key.'&nonce='.$nonce;
            $sign=hash_hmac('sha512', $uri, $user->bit_api_secret);
            $ch = curl_init($uri);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('apisign:'.$sign));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            $execResult = curl_exec($ch);
            $obj = json_decode($execResult, true)['result'];
            $total_btc = 0;
            $btc_price = 9100;
            $usd_to_btc = 0;
            $usd = 0; 
            foreach($obj as $result) {
                if($result['Currency'] == 'BTC') ## SE FOR BITCOIN
                    $btc = $result['Balance'];   ##SALDO DISPONIVEL EM BTC
                if($result['Currency'] == 'USDT') {  ## SE FOR DOLAR 
                    $usd_to_btc = floatval($result['Balance'])/$btc_price; ##CONVERTENDO SALDO EM USDT PARA BTC
                    $usd = $result['Balance']; ##SALDO USDT DISPONIVEL
                }
                if($result['Balance'] != 0 and $result['Currency'] != 'USDT' and $result['Currency'] != 'BTC') {
                    $file = file_get_contents("https://bittrex.com/api/v1.1/public/getticker?market=BTC-".$result['Currency']);
                    $data = json_decode($file, true);
                    $value_in_btc = $data['result']['Bid'];
                    $convert = $result['Balance']*$value_in_btc;
                    $total_btc = $total_btc + $convert;
                }
            }
            if($currency == 'USDT') {
                $total = ($total_btc+$btc)*$btc_price;
                return number_format($total+$usd, 2, '.', ' ');
            }
            ############
            return number_format($total_btc + $btc + $usd_to_btc, 8, '.', ' ');
        }
        return 'Não conectado.';
    }

    public function check_bittrex() {
        $nonce=time();
        $user = Auth::user();
        $uri = 'https://bittrex.com/api/v1.1/account/getbalance?apikey='.$user->bit_api_key.'&nonce='.$nonce.'&currency=BTC';
        $sign = hash_hmac('sha512', $uri, $user->bit_api_secret);
        $ch = curl_init($uri);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('apisign:'.$sign));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $execResult = curl_exec($ch);
        $obj = json_decode($execResult, true);
        return $obj["success"];
    }

    ##BINANCE
    public function update_api_binance(Request $request) {
        $user = Auth::user();
        $user->bin_api_secret = UserController::test_input($request['bin_api_secret']);
        $user->bin_api_key = UserController::test_input($request['bin_api_key']);
        $user->save();
        return redirect()->route('account');
    }

    public function binance_balance($currency) {
        $params = [];
        $user = Auth::user();
        if($user->premium > 0 and strlen($user->bin_api_key) > 0 and strlen($user->bin_api_secret)) {
            $headers[] = "User-Agent: Mozilla/4.0 (compatible; PHP Binance API)\r\nX-MBX-APIKEY: {$user->bin_api_key}\r\n";
            $params['timestamp'] = number_format(microtime(true) * 1000, 0, '.', '');
            $query = http_build_query($params, '', '&');
            $signature = hash_hmac('sha256', $query, $user->bin_api_secret);
            $endpoint = "https://www.binance.com/api/v3/account?{$query}&signature={$signature}";
            $balances = json_decode(UserController::http_request($endpoint, $headers), true)['balances'];
            #################
            $btc_price = UserController::btc_price();
            $total_btc = 0;
            foreach($balances as $b) {
                if($b['asset'] == 'BTC')
                    $btc = $b['free']; ##SALDO EM BTC DISPONIVEL
                if($b['asset'] == 'USDT') {
                    $usd_to_btc = floatval($b['free'])/$btc_price; ##CONVERTENDO SALDO EM USDT PARA BTC
                    $usd = $b['free']; ##SALDO USDT DISPONIVEL
                }
                if($b['free'] != 0 and $b['asset'] != 'USDT' and $b['asset'] != 'BTC') {
                    $file = file_get_contents("https://www.binance.com/api/v3/ticker/price?symbol=".$b['asset']."BTC");
                    $data = json_decode($file, true);
                    $value_in_btc = $data['price']; ##VALOR DA MOEDA EM BITCOIN
                    $convert = $b['free']*$value_in_btc; ##CONVERTENDO TOTAL DE MOEDAS ALT EM BITCOIN
                    $total_btc = $total_btc + $convert;  ##FAZENDO UM TOTAL DISSO PARA TODAS ALTCOINS COM SALDO > 0
                }
            }
            ##########
            if($currency == 'USDT') {
                $total = ($total_btc+$btc)*$btc_price;
                return number_format($total+$usd, 2, '.', ' ');
            }
            ############
            return number_format($total_btc + $btc + $usd_to_btc, 8, '.', ' ');
        }
        return 'Não conectado.';
    }

    public function check_binance() {
        $params = [];
        $user = Auth::user();
        $headers[] = "User-Agent: Mozilla/4.0 (compatible; PHP Binance API)\r\nX-MBX-APIKEY: {$user->bin_api_key}\r\n";
        $params['timestamp'] = number_format(microtime(true) * 1000, 0, '.', '');
        $query = http_build_query($params, '', '&');
        $signature = hash_hmac('sha256', $query, $user->bin_api_secret);
        $endpoint = "https://www.binance.com/api/v3/account?{$query}&signature={$signature}";
        $balances = json_decode(UserController::http_request($endpoint, $headers), true);
        if(empty($balances['balances'])){
            return 0;
        }
        return 1;
    }

    public function http_request($url, $headers, $data = array()) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        if ($data) {
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        }
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_TIMEOUT, 5);
        curl_setopt($ch, CURLOPT_ENCODING, "");
        $content = curl_exec($ch);
        if (curl_errno($ch)) {
            $content = false;
        }
        curl_close($ch);
        return $content;
    }

    public function btc_price() {
        $URL = file_get_contents("https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT");
        return json_decode($URL, true)['price'];
    }


}
