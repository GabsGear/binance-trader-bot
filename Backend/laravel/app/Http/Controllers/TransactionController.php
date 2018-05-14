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
        $bot = Bot::find($t->bot_id);
        if($bot->exchange == 'binance') {
            $fee = $delta*0.001;
        } else {
            $fee = $delta*0.005;
        }
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
        ->select('transactions.*', 'bot.currency', 'bot.exchange')
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
    
    public function show_stats() {
        ##REQUISITANDO TRANSACOES DAS ESTRATEGIAS
        $trans_pivot = TransactionController::show_strategy(3);
        $trans_rsi = TransactionController::show_strategy(4);
        $trans_break = TransactionController::show_strategy(6);
        ##RETORNANDO DADOS COMPACTADOS DE CADA ESTRATEGIA
        $data_pivot = TransactionController::show_profit($trans_pivot);
        $data_rsi = TransactionController::show_profit($trans_rsi);
        $data_break = TransactionController::show_profit($trans_break);
        ##TAXA DE ACERTO
        $pivot_tax = ($data_pivot[2]/($data_pivot[2]+$data_pivot[3]))*100;
        $rsi_tax = ($data_rsi[2]/($data_rsi[2]+$data_rsi[3]))*100;
        $break_tax = ($data_break[2]/($data_break[2]+$data_break[3]))*100;
        ##RETORNANDO PRA VIEW OS DADOS
        echo  "
            Inicio dos logs: 29/04/2018 | Capital investido: 1 BTC
            </br></br>
            <table border='1px solid black' cellspacing='10'>
                <tr>
                    <td>Estratégia</td>
                    <td>Ganhos Total dos Bots BTC</td>
                    <td>Ganhos Total dos Bots USDT</td>
                    <td>Acertos/Erros</td>
                    <td>Taxa de Acerto</td>
                </tr>
                <tr>
                    <td>Pivo de Alta</td>
                    <td>".$data_pivot[0]." BTC</td>
                    <td>".$data_pivot[1]." USDT</td>
                    <td>".$data_pivot[2]."/".$data_pivot[3]."</td>
                    <td>".$pivot_tax." %</td>
                </tr>
                <tr>
                    <td>Indice de Forca</td>
                    <td>".$data_rsi[0]." BTC</td>
                    <td>".$data_rsi[1]." USDT</td>
                    <td>".$data_rsi[2]."/".$data_rsi[3]."</td>
                    <td>".$rsi_tax." %</td>
                </tr>
                <tr>
                    <td>Quebra de Canal</td>
                    <td>".$data_break[0]." BTC</td>
                    <td>".$data_break[1]." USDT</td>
                    <td>".$data_break[2]."/".$data_break[3]."</td>
                    <td>".$break_tax." %</td>
                </tr>
            </table>
        ";
        echo TransactionController::capital_acumulado();
    }

    public function show_profit($dict) {
        $total_btc = 0;
        $total_usd = 0;
        $total_acerto = 0;
        $total_erro = 0;
        foreach($dict as $t) {
            $cur = explode("-", $t->currency);
            $lucro  = ($t->sell_value-$t->buy_value)*$t->quantity;
            if($cur[0] == 'USDT' ){
                $total_usd = $total_usd + $lucro;
            }
            if($cur[0] == 'BTC' ){
                $total_btc = $total_btc + $lucro;
            }
            if($lucro > 0) {
                $total_acerto = $total_acerto + 1;
            }else {
                $total_erro = $total_erro + 1;
            }
        }
        return array($total_btc, $total_usd, $total_acerto, $total_erro);
    }

    public function show_strategy($id) {
        $trans = DB::table('bot')
        ->join('transactions', 'transactions.bot_id', '=', 'bot.id')
        ->select('transactions.*', 'bot.strategy_buy', 'bot.currency', 'bot.user_id')
        ->where('transactions.selled', 1)
        ->where('bot.strategy_buy', $id)
        ->where('bot.user_id', 6)
        ->get();
        return $trans;
    }


    public function capital_acumulado($id) {
        $capital = 0.05;
        $capital_inicial = 0.05;
        $i = 0; 
        $acerto = 0;
        $erro = 0;
        $vec_x = array('0.05');
        $trans = DB::table('transactions')
        ->where('bot_id', $id)
        ->where('selled', 1)
        ->get();
        $bot = Bot::find($id);
        echo "</br></br>";
        echo "PAR:".$bot->currency."</br>";
        echo "ID: ".$bot->id." | Strategy: ".$bot->strategy_buy." | Profit: ".$bot->percentage." | Stoploss: ".$bot->stoploss;
        echo "</br>
        -----------------------------------------------------------
        </br>";
        foreach($trans as $t) {
            $trade  = ($t->sell_value-$t->buy_value)*$t->quantity;
            $fee = $trade*0.002;
            if($trade > 0) {
                echo "[OP-".$i."] Saldo:".$capital."+".$trade."|fee:".$fee."-</br>";
                echo "Open:".$t->date_open." | Close:".$t->date_close."</br>";
                $acerto = $acerto + 1;
            }
            else {
                echo "[OP-".$i."] Saldo:".$capital."".$trade."|fee:".$fee."-</br>";
                $erro = $erro + 1;
            }
            $capital = $capital + $trade - $fee;
            echo "----------------------</br>
            Subtotal:
            ".$capital."</br>------------------</br>";
            $i = $i+1;
            array_push($vec_x, $capital);
        }
        echo "</br>
        -----------------------------------------------------------
        </br>";
        $l = $capital - $capital_inicial;
        $percentage = ($l*100/$capital_inicial);
        echo "</br>Total:".$capital;
        echo "</br>Inicial USD:".$capital_inicial*8600;
        echo "</br>Final USD:".$capital*8600;
        echo "</br>Porcentagem de ganho:".$percentage."%";
        echo "</br>Acerto:".$acerto;
        echo "</br>Erros:".$erro."</br>";
        /*foreach($vec_x as $x) {
            echo $x."</br>";
        }*/
        $drowndawn = (min($vec_x)-max($vec_x))/max($vec_x);
        echo "</br>Max-gain: ".max($vec_x)."</br>";
        echo "</br>Min-gain: ".min($vec_x)."</br>";
        echo "</br>Drowndawn-max: ".$drowndawn."</br>";
 
    }
  

}