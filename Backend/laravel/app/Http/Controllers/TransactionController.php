<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Transaction;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use DB;
use Auth;
use App\Bot;
use App\Http\Controllers\BotController;

class TransactionController extends Controller
{

    public function getAllTrans() {
        $bots = DB::table('bot')->where('user_id', Auth::User()->id)->get();
        $total = 0;
        foreach($bots as $bot) {
            $count = DB::table('transactions')->where('bot_id', $bot->id)->get()->count();
            $total = $total + $count;
        }
        return $total;
    }

    public function getTrans($bot_id) {
        $bot = Bot::find($bot_id);
        if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
            return redirect()->route('dashboard');
        $trans = DB::table('transactions')->where('bot_id', $bot_id)->orderBy('id', 'desc')->get()->take(1);
        return $trans;
    }

    public function getAllNotSelled() {
        $bots = DB::table('bot')->where('user_id', Auth::User()->id)->get();
        $trans = array();
        foreach ($bots as $bot) {
            $t = DB::table('transactions')->where('selled', 0)->where('bot_id', $bot->id)->get();
            foreach ($t as $v) {
                array_push($trans, $v);
            }
        }
        array_multisort(array_map(function($element) {
            return $element->id;
        }, $trans), SORT_DESC, $trans);
        return $trans;
    }

    public function getAllSelled() {
        $bots = DB::table('bot')->where('user_id', Auth::User()->id)->get();
        $trans = array();
        foreach ($bots as $bot) {
            $t = DB::table('transactions')->where('selled', 1)->where('bot_id', $bot->id)->get();
            foreach ($t as $v) {
                array_push($trans, $v);
            }
        }
        array_multisort(array_map(function($element) {
            return $element->id;
        }, $trans), SORT_DESC, $trans);
        return $trans;
    }


    public static function btcPrice() {
        $str = file_get_contents('https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC');
        $json = json_decode($str, true);
        return $json['result']['Bid'];
    }

    public function getTotal($bot_id) {
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
    	return $total*TransactionController::btcPrice()*3.3;
    }

    public function getPercentage($sell, $buy) {
        $x = $sell*100/$buy;
        if($x < 100) {
            return -1*(100-$x);
        }
        elseif($x == 100) {
            return 0;
        }else {
            return $x-100;
        }
    }

    public function getTotalTrades($bot_id){
        $bot = Bot::find($bot_id);
        if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
            return redirect()->route('dashboard');
        return DB::table('transactions')->where('bot_id', $bot_id)->get()->count();
    }

    public function getAllTotal() {
        $bots = DB::table('bot')->where('user_id', Auth::User()->id)->get();
        $count = DB::table('transactions')->where('selled', 1)->get()->count();
        $total_btc = 0;
        $total_usd = 0;
        if($count > 0) {
        	foreach ($bots as $bot) {
                $tag = explode('-', $bot->currency);
                $trans = DB::table('transactions')->where('bot_id', $bot->id)->get();
                foreach($trans as $t) {
            		if($t->selled == 1) {
            			$lucro = $t->sell_value-$t->buy_value;
                        $qnt = $lucro*$t->quantity;
                        if($tag[0] == 'USDT' ) {
                            $total_usd = $total_usd + $qnt;
                        }
                        if($tag[0] == 'BTC' ){
                            $total_btc = $total_btc + $qnt;
                        }
            		}
                }
        	}
        	return ($total_usd*3.3)+($total_btc*TransactionController::btcPrice()*3.3);
        } else {
            return 0;
        }
    }

  

}