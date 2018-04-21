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
        ->select('transactions.*', 'bot.currency')
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
        ->select('transactions.*')
        ->where('bot.user_id', Auth::User()->id)
        ->whereDate('date_close', '=', $date)
        ->get();
        return view('reportsclose', compact('trans'));
    }
    
    public function filter_name(Request $request) {
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*')
        ->where('bot.user_id', Auth::User()->id)
        ->where('bot.name', $request['name'])
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
    	foreach ($all as $trans) {
    		if($trans->selled != 0){
    			$lucro = $trans->sell_value-$trans->buy_value;
    			$qnt = $lucro*$trans->quantity;
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
                if($t->selled == 1) {
                    $lucro = $t->sell_value-$t->buy_value;
                    $qnt = $lucro*$t->quantity;
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

  

}