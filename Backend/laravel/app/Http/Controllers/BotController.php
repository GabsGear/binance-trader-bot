<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use Charts;
use App\Transaction;
use App\Bot;
use DB;
use Auth;
use App\Http\Controllers\TransactionController;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Redirect;

class BotController extends Controller
{

    public function getCurrency($id) {
        return Bot::find($id)->currency;
    }

    public function create(Request $request) {
        try {
            $markets_bitrex = ['BTC-2GIVE','BTC-ABY','BTC-ADA','BTC-ADT','BTC-ADX','BTC-AEON','BTC-AMP','BTC-ANT','BTC-ARDR','BTC-ARK','BTC-AUR','BTC-BAT','BTC-BAY','BTC-BCC','BTC-BCPT','BTC-BCY','BTC-BITB','BTC-BLITZ','BTC-BLK','BTC-BLOCK','BTC-BNT','BTC-BRK','BTC-BRX','BTC-BSD','BTC-BTG','BTC-BURST','BTC-BYC','BTC-CANN','BTC-CFI','BTC-CLAM','BTC-CLOAK','BTC-COVAL','BTC-CRB','BTC-CRW','BTC-CURE','BTC-CVC','BTC-DASH','BTC-DCR','BTC-DCT','BTC-DGB','BTC-DMD','BTC-DMT','BTC-DNT','BTC-DOGE','BTC-DOPE','BTC-DTB','BTC-DYN','BTC-EBST','BTC-EDG','BTC-EFL','BTC-EGC','BTC-EMC','BTC-EMC2','BTC-ENG','BTC-ENRG','BTC-ERC','BTC-ETC','BTC-ETH','BTC-EXCL','BTC-EXP','BTC-FCT','BTC-FLDC','BTC-FLO','BTC-FTC','BTC-GAM','BTC-GAME','BTC-GBG','BTC-GBYTE','BTC-GEO','BTC-GLD','BTC-GNO','BTC-GNT','BTC-GOLOS','BTC-GRC','BTC-GRS','BTC-GUP','BTC-HMQ','BTC-IGNIS','BTC-INCNT','BTC-IOC','BTC-ION','BTC-IOP','BTC-KMD','BTC-KORE','BTC-LBC','BTC-LGD','BTC-LMC','BTC-LRC','BTC-LSK','BTC-LTC','BTC-LUN','BTC-MANA','BTC-MCO','BTC-MEME','BTC-MER','BTC-MLN','BTC-MONA','BTC-MUE','BTC-MUSIC','BTC-NAV','BTC-NBT','BTC-NEO','BTC-NEOS','BTC-NLG','BTC-NMR','BTC-NXC','BTC-NXS','BTC-NXT','BTC-OK','BTC-OMG','BTC-OMNI','BTC-PART','BTC-PAY','BTC-PINK','BTC-PIVX','BTC-PKB','BTC-POT','BTC-POWR','BTC-PPC','BTC-PTC','BTC-PTOY','BTC-QRL','BTC-QTUM','BTC-QWARK','BTC-RADS','BTC-RBY','BTC-RCN','BTC-RDD','BTC-REP','BTC-RLC','BTC-RVR','BTC-SALT','BTC-SBD','BTC-SC','BTC-SEQ','BTC-SHIFT','BTC-SIB','BTC-SLR','BTC-SLS','BTC-SNRG','BTC-SNT','BTC-SPHR','BTC-SPR','BTC-SRN','BTC-STEEM','BTC-STORJ','BTC-STRAT','BTC-SWIFT','BTC-SWT','BTC-SYNX','BTC-SYS','BTC-THC','BTC-TIX','BTC-TKS','BTC-TRST','BTC-TRUST','BTC-TRX','BTC-TUSD','BTC-TX','BTC-UBQ','BTC-UKG','BTC-UNB','BTC-UP','BTC-VEE','BTC-VIA','BTC-VIB','BTC-VRC','BTC-VRM','BTC-VTC','BTC-VTR','BTC-WAVES','BTC-WAX','BTC-WINGS','BTC-XCP','BTC-XDN','BTC-XEL','BTC-XEM','BTC-XLM','BTC-XMG','BTC-XMR','BTC-XMY','BTC-XRP','BTC-XST','BTC-XVC','BTC-XVG','BTC-XWC','BTC-XZC','BTC-ZCL','BTC-ZEC','BTC-ZEN','BTC-ZRX','USDT-ADA','USDT-BCC','USDT-BTC','USDT-BTG','USDT-DASH','USDT-ETC','USDT-ETH','USDT-LTC','USDT-NEO','USDT-NXT','USDT-OMG','USDT-TUSD','USDT-XMR','USDT-XRP','USDT-XVG','USDT-ZEC'];
            $markets_binance = ['USDT-BTC', 'USDT-ETH', 'USDT-BNB', 'USDT-BCC', 'USDT-NEO', 'USDT-LTC', 'USDT-QTUM', 'BTC-ETH', 'BTC-LTC', 'BTC-BNB', 'BTC-NEO', 'BTC-BCC', 'BTC-GAS', 'BTC-HSR', 'BTC-MCO', 'BTC-WTC', 'BTC-LRC', 'BTC-QTUM', 'BTC-YOYO', 'BTC-OMG', 'BTC-ZRX', 'BTC-STRAT', 'BTC-SNGLS', 'BTC-BQX', 'BTC-KNC', 'BTC-FUN', 'BTC-SNM', 'BTC-IOTA', 'BTC-LINK', 'BTC-XVG', 'BTC-SALT', 'BTC-MDA', 'BTC-MTL', 'BTC-SUB', 'BTC-EOS', 'BTC-SNT', 'BTC-ETC', 'BTC-MTH', 'BTC-ENG', 'BTC-DNT', 'BTC-ZEC', 'BTC-BNT', 'BTC-AST', 'BTC-DASH', 'BTC-OAX', 'BTC-ICN', 'BTC-BTG', 'BTC-EVX', 'BTC-REQ', 'BTC-VIB', 'BTC-TRX', 'BTC-POWR', 'BTC-ARK', 'BTC-XRP', 'BTC-MOD', 'BTC-ENJ', 'BTC-STORJ', 'BTC-VEN', 'BTC-KMD', 'BTC-RCN', 'BTC-NULS', 'BTC-RDN', 'BTC-XMR', 'BTC-DLT', 'BTC-AMB', 'BTC-BAT', 'BTC-BCPT', 'BTC-ARN', 'BTC-GVT', 'BTC-CDT', 'BTC-GXS', 'BTC-POE', 'BTC-QSP', 'BTC-BTS', 'BTC-XZC', 'BTC-LSK', 'BTC-TNT', 'BTC-FUEL', 'BTC-MANA', 'BTC-BCD', 'BTC-DGD', 'BTC-ADX', 'BTC-ADA', 'BTC-PPT', 'BTC-CMT', 'BTC-XLM', 'BTC-CND', 'BTC-LEND', 'BTC-WABI', 'BTC-TNB', 'BTC-WAVES', 'BTC-GTO', 'BTC-ICX', 'BTC-OST', 'BTC-ELF', 'BTC-AION', 'BTC-NEBL', 'BTC-BRD', 'BTC-EDO', 'BTC-WINGS', 'BTC-NAV', 'BTC-LUN', 'BTC-TRIG', 'BTC-APPC', 'BTC-VIBE', 'BTC-RLC', 'BTC-INS', 'BTC-PIVX', 'BTC-IOST', 'BTC-CHAT', 'BTC-STEEM', 'BTC-NANO', 'BTC-VIA', 'BTC-BLZ', 'BTC-AE', 'BTC-RPX', 'BTC-NCASH', 'BTC-POA', 'BTC-ZIL', 'BTC-ONT', 'BTC-STORM', 'BTC-XEM', 'BTC-WAN', 'BTC-WPR', 'BTC-QLC', 'BTC-SYS', 'BTC-GRS'];
            $count_bots = BotController::getAllBots()->count();
            
            ##VALIDACAO
            if($count_bots >= 2 && Auth::user()->premium == 0)
                return Redirect::back()->withErrors(['Você atingiu o limite de bots permitido.']);
            if($count_bots >= 5 && Auth::user()->premium == 1)
                return Redirect::back()->withErrors(['Você atingiu o limite de bots permitido.']);
            if($count_bots >= 10 && Auth::user()->premium == 2)
                return Redirect::back()->withErrors(['Você atingiu o limite de bots permitido.']);
            if($count_bots >= 30 && Auth::user()->premium == 3)
                return Redirect::back()->withErrors(['Você atingiu o limite de bots permitido.']);
            ############
            
            $bot = new Bot;
            $bot->user_id = Auth::user()->id;
            $bot->name = str_random(8);
            $bot->exchange = BotController::test_input($request['exchange']);
            $bot->currency = BotController::test_input($request['currency']);
            if($bot->exchange == 'bittrex') {
                if(in_array($bot->currency, $markets_bitrex) == false) {
                    return Redirect::back()->withErrors(['Insira um mercado válido.']);
                };
            }else {
                if(in_array($bot->currency, $markets_binance) == false) {
                    return Redirect::back()->withErrors(['Insira um mercado válido.']);
                };
            }
            $piece = explode("-", $bot->currency );
            if($piece[0] == 'USDT') {
                $bot->order_value = 5000.0;
            }
            else {
                $bot->order_value = 0.05;
            }
            $bot->strategy_buy = BotController::test_input($request['strategy_buy']);
            $bot->percentage = BotController::test_input($request['percentage']);
            $bot->pid = 0;
            $bot->active = 2;
            $bot->order_value = 0.05;
            $bot->period = BotController::test_input($request['period']);
            $bot->stoploss = BotController::test_input($request['stoploss']);
            $bot->save();
            unset($_POST);
            return redirect()->route('dashboard');
        } catch (Exception $e) {
            dd($e);
            return "erro";
        }
    }

    public function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    public function getMarket($id) {
        $bot = Bot::find($id);
        $tag = explode('-', $bot->currency);
        return $tag[0];
    }

    public static function getCandles($id) {
        try{
            $bot = Bot::find($id);
            if(Auth::user()->id != $bot->user_id)
                return redirect()->route('dashboard');
            $obj = file_get_contents("https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=".$bot->currency."&tickInterval=".$bot->period);
            return $obj;
        } catch(Exception $e) {
            dd($e);
            return "Erro getCandles.";
        }
    }


    public function stopAll() {
        try {
            $bots = Bot::All();
            foreach ($bots as $bot) {
                if(Auth::user()->id == $bot->user_id and $bot->active == 1) {
                    $bot->active = 2;
                    $bot->save();
                }
                if(Auth::user()->id == $bot->user_id and $bot->active == 0) {
                    $bot->active = 2;
                    $bot->save();
                }
            }
            return redirect()->route('dashboard');
        } catch (Exception $e) {
            dd($e);
            return "erro";
        }
    }

    public function updateWallet(Request $request, $id) {
        try {
            $bot = Bot::find($id);
            if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
                return redirect()->route('dashboard');
            $bot->order_value = $request['order_value'];
            $bot->save();
            return redirect()->route('dashboard');
        } catch (Exception $e) {
            dd($e);
            return "erro";
        }
    }

    public function active(Request $request) {
        try {
            $bot = Bot::find($request['id']);
            if(Auth::User()->premium == 0 or Auth::user()->id != $bot->user_id)
                return redirect()->route('dashboard');
            $bot->active = $request['active'];
            $bot->save();
            return redirect()->route('dashboard');
        } catch (Exception $e) {
            dd($e);
            return "Erro na troca de modo de operacao.";
        }
    }

    public function getAllBots() {
        return DB::table('bot')->where('user_id', Auth::user()->id)->get();
    }

    public function countBots($status) {
        return DB::table('bot')->where('user_id', Auth::user()->id)->where('active', $status)->get()->count();
    }

    public function getAllBotTransactions($id) {
        $bot = Bot::find($id);
        if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
            return redirect()->route('dashboard');
        return DB::table('transactions')->where('bot_id', $id)->get();
    }

    public function getTotalPercentage($id) {
        $trans = DB::table('transactions')->where('bot_id', $id)->get();
        $total = 0;
        $totalf = 0;
        foreach($trans as $t) {
            if($t->selled == 1 and $t->buy_value != $t->sell_value){
                $total = $total + (TransactionController::getPercentage($t->sell_value, $t->buy_value));
                $totalf = $totalf + (TransactionController::getPercentage($t->sell_value, $t->buy_value)-0.25);
            
            }
        }
        echo "total bruto:".$total."%</br>";
        echo "total c/ fee:".$totalf."%";
    }

    public function getAllCurrencys() {
        return DB::table('bot')->select('currency')->distinct()->where('user_id', Auth::user()->id)->get()->count();
    }

    public function destroy($id) {
        $bot = Bot::find($id);
        if(Auth::user()->id != $bot->user_id)  //verificacao de seguranca
            return redirect()->route('dashboard');
        $pid = $bot->pid;
        $count = DB::table('transactions')->where('bot_id', $id)->get()->count();
        shell_exec('sudo kill -9 '.$bot->pid.' > /dev/null &');
        Bot::where('id', $id)->delete();
        if($count > 0)
            DB::table('transactions')->where('bot_id', $id)->delete();
        return redirect()->route('dashboard');
    }


}