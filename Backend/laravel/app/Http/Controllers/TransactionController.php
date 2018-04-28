<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use DB;
use Auth;
use App\Bot;
use App\Http\Controllers\BotController;

class TransactionController extends Controller
{

    ##Retorna as ultimas 50 transacoes do usuario
    ##param: selled pode ser 0 para ordem aberta e 1 para ordens fechadas
    public static function getAll($selled) {
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.currency', 'bot.exchange')
        ->where('bot.user_id', Auth::User()->id)
        ->where('transactions.selled', $selled)
        ->orderBy('transactions.id', 'desc')
        ->get()->take(50);
        return $trans;
    }

    public function filter_date(Request $request) {
        $date = $request['date'];
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.currency', 'bot.exchange')
        ->where('bot.user_id', Auth::User()->id)
        ->whereDate('date_close', '=', $date)
        ->where('transactions.selled', 1)
        ->get();
        return view('reportsclose', compact('trans'));
    }
    
    public function convert_date($date) {
        $slice_1 = explode(' ', $date);
        $slice_2 = explode('-', $slice_1[0]);
        return $slice_2[2]."/".$slice_2[1]."/".$slice_2[0]."-".$slice_1[1];
    }
    
    public function filter_name(Request $request) {
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.currency', 'bot.exchange')
        ->where('bot.user_id', Auth::User()->id)
        ->where('bot.name', $request['name'])
        ->where('transactions.selled', 1)
        ->get();
        return view('reportsclose', compact('trans'));
    }

    public static function btcPrice() {
        $str = file_get_contents('https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC');
        $json = json_decode($str, true);
        return $json['result']['Bid'];
    }


    ##CALCULA A PORCENTAGEM DE VARIACAO ENTRE OS PRECOS DE COMPRA E VENDA
    ##PARAMETRO PRECO SE VENDA,COMPRA RESPECTIVAMENTE
    public function getPercentage($t) {
        $x = $t->sell_value*100/$t->buy_value;
        if($x < 100) {
            return -1*(100-$x);
        }
        elseif($x == 100) {
            return 0;
        }else {
            return $x-100;
        }
    }

    public function getFee($t) {
        $delta = ($t->sell_value-$t->buy_value)*$t->quantity;
        $fee = $delta*0.005;
        if($fee < 0)
            $fee = $fee*(-1);
        return $fee;
    }

    ##CONTAGEM DE TODAS TRANSACOES
    ##PARAMETRO SELLED DA TRANSACACAO
    public function count($selled){
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->where('bot.user_id', Auth::User()->id)
        ->where('selled', $selled)
        ->get()->count();
        return $trans;
    }


    ##LEVANTAMENTO TOTAL DO SALDO DE UM BOT
    ##PARAMETRO ID DO BOT
    public function getBalance($bot_id) {
        $bot = Bot::find($bot_id);
        $tag = explode('-', $bot->currency);
        if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
            return redirect()->route('dashboard');
    	$all = DB::table('transactions')->where('bot_id', $bot_id)->get();
    	$total = 0;
    	foreach ($all as $t) {
    		if($t->selled != 0){
                $fee = TransactionController::getFee($t);
    			$lucro = $t->sell_value-$t->buy_value;
    			$qnt = ($lucro*$t->quantity)-$fee;
    			$total = $total + $qnt;
    		}
        }
        if($tag[0] == 'USDT'){
            return $total*3.3;
        }	
    	return $total*8100*3.3;
    }

    ##LEVANTAMENTO TOTAL DO SALDO
    public function getBalanceTotal() {
        $total_btc = 0;
        $total_usd = 0;
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.currency')
        ->where('bot.user_id', Auth::User()->id)
        ->get();
        if($trans->count() > 0) {
        	foreach ($trans as $t) {
                $market = explode('-', $t->currency);
                $fee = TransactionController::getFee($t);
                if($t->selled == 1) {
                    $lucro = $t->sell_value-$t->buy_value;
                    $qnt = ($lucro*$t->quantity)-$fee;
                    if($market[0] == 'USDT' ) {
                        $total_usd = $total_usd + $qnt;
                    }
                    if($market[0] == 'BTC' ){
                        $total_btc = $total_btc + $qnt;
                    }
                }
        	}
        	return ($total_usd*3.3)+($total_btc*8100*3.3);
        } else {
            return 0;
        }
    }

    public function destroy($id) {
        DB::table('transactions')->where('id', $id)->delete();
        return redirect()->back();
    }
    
    public function clean_db() {
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.strategy_buy', 'bot.currency')
        ->where('transactions.selled', 1)
        ->get();
        $total_tt = array(0, 0); //MEDIDA DE GANHO/PERCA 0
        $total_ib = array(0, 0); //MEDIDA DE GANHO/PERCA 1
        $total_du = array(0, 0); //MEDIDA DE GANHO/PERCA 2
        $total_pu = array(0, 0); //MEDIDA DE GANHO/PERCA 3
        foreach($trans as $t) {
            if($t->strategy_buy == 0 and $t->currency != 'BTC-DOGE') { // CONTRA TURTLE
                if($t->buy_value <= $t->sell_value) { // LUCRO
                    $var = TransactionController::getPercentage($t);
                    $total_tt[0] = $total_tt[0] + 1;  //CALCULANDO TOTAL DE VEZES QUE GANHOU
                } else { // PREJUIZO
                    $total_tt[1] = $total_tt[1] + 1;  //CALCULANDO TOTAL DE VEZES QUE PERDEU
                }
            }
            ###################################
            if($t->strategy_buy == 1 and $t->currency != 'BTC-DOGE') { // CONTRA TURTLE
                if($t->buy_value <= $t->sell_value) { // LUCRO
                    $var = TransactionController::getPercentage($t);
                    $total_ib[0] = $total_ib[0] + 1;  //CALCULANDO TOTAL DE VEZES QUE GANHOU
                } else { // PREJUIZO
                    $total_ib[1] = $total_ib[1] + 1;  //CALCULANDO TOTAL DE VEZES QUE PERDEU
                }
            }
            ##################################
            if($t->strategy_buy == 2 and $t->currency != 'BTC-DOGE') { // CONTRA TURTLE
                if($t->buy_value <= $t->sell_value) { // LUCRO
                    $var = TransactionController::getPercentage($t);
                    $total_du[0] = $total_du[0] + 1;  //CALCULANDO TOTAL DE VEZES QUE GANHOU
                } else { // PREJUIZO
                    $total_du[1] = $total_du[1] + 1;  //CALCULANDO TOTAL DE VEZES QUE PERDEU
                }
            }
            ################################
            if($t->strategy_buy == 4 and $t->currency != 'BTC-DOGE') { // CONTRA TURTLE
                if($t->buy_value <= $t->sell_value) { // LUCRO
                    $var = TransactionController::getPercentage($t);
                    $total_pu[0] = $total_pu[0] + 1;  //CALCULANDO TOTAL DE VEZES QUE GANHOU
                } else { // PREJUIZO
                    $total_pu[1] = $total_pu[1] + 1;  //CALCULANDO TOTAL DE VEZES QUE PERDEU
                }
            }
        }
       // $tx_acerto_tt = ($total_tt[1]/$total_tt[0])*100;
        //$tx_acerto_ib = ($total_ib[1]/$total_ib[0])*100;
        //$tx_acerto_du = ($total_du[1]/$total_du[0])*100;
        //$tx_acerto_pu = ($total_pu[1]/$total_pu[0])*100;
        //echo "|CONTRA TURTLE|TAXA DE ACERTO:".$tx_acerto_tt."%|</br>";
        //echo "|CONTRA TURTLE|TAXA DE ACERTO:".$tx_acerto_ib."%|</br>";
        //echo "|CONTRA TURTLE|TAXA DE ACERTO:".$tx_acerto_du."%|</br>";
        //echo "|CONTRA TURTLE|TAXA DE ACERTO:".$tx_acerto_pu."%|</br>";
        var_dump($total_tt);
        var_dump($total_ib);
        var_dump($total_du);
        var_dump($total_pu);
    }
  

}