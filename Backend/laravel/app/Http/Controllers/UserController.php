<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use Auth;
use Hash;


class UserController extends Controller
{

    public function getUser() {
        return Auth::user();
    }

    public function reset(Request $request) {
        $current_password = Auth::User()->password;           
        if(Hash::check($request->input('oldpass'), $current_password) AND $request->input('password') == $request->input('password_confirmation')) {           
            $user_id = Auth::User()->id;                       
            $obj_user = User::find($user_id);
            $obj_user->password = Hash::make($request->input('password'));
            $obj_user->save(); 
        }
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
        $nonce=time();
        $user = Auth::user();
        $uri='https://bittrex.com/api/v1.1/account/getbalance?apikey='.$user->bit_api_key.'&nonce='.$nonce.'&currency='.$currency;
        $sign=hash_hmac('sha512', $uri, $user->bit_api_secret);
        $ch = curl_init($uri);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('apisign:'.$sign));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $execResult = curl_exec($ch);
        $obj = json_decode($execResult, true);
        if($currency == 'USDT' and $obj['result']['Balance'] < 1.0){
            return 0;
        }
        return $obj['result']['Balance']; 
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
        $headers[] = "User-Agent: Mozilla/4.0 (compatible; PHP Binance API)\r\nX-MBX-APIKEY: {$user->bin_api_key}\r\n";
        $params['timestamp'] = number_format(microtime(true) * 1000, 0, '.', '');
        $query = http_build_query($params, '', '&');
        $signature = hash_hmac('sha256', $query, $user->bin_api_secret);
        $endpoint = "https://www.binance.com/api/v3/account?{$query}&signature={$signature}";
        $balances = json_decode(UserController::http_request($endpoint, $headers), true)['balances'];
        foreach($balances as $b) {
            if($b['asset'] == $currency) {
                return floatval($b['free'])+floatval($b['locked']);
            }
        }
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


}
