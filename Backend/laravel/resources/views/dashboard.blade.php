@inject('BotController', 'App\Http\Controllers\BotController')
@inject('TransactionController', 'App\Http\Controllers\TransactionController')
@inject('ProcessController', 'App\Http\Controllers\ProcessController')


@extends('layouts/default')
@section('content')
<header class="head">
    <div class="main-bar">
       <div class="row no-gutters">
           <div class="col-6">
               <h4 class="m-t-5">
                   <i class="fa fa-home"></i>
                   Inicio
               </h4>
           </div>
       </div>
    </div>
</header>
<div class="outer">
    <div class="inner bg-container">
        <div class="row">
            <div class="col-12">
                <div class="row">
                    <div class="col-sm-3 col-12">
                        <div class="bg-primary top_cards"> <!--CARD COMEÇO -->
                            <div class="row icon_margin_left">
                                <div class="col-5 icon_padd_left">
                                    <div class="float-left">
                                        <span class="fa-stack fa-sm">
                                        <i class="fa fa-circle fa-stack-2x"></i>
                                        <i class="fa fa-android fa-stack-1x fa-inverse text-primary sales_hover"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="col-7 icon_padd_right">
                                    <div class="float-right cards_content">
                                        <span class="number_val">{{$BotController->getAllBots()->count()}}</span>
                                        <br/>
                                        <span class="card_description">Bots Ativos</span>
                                    </div>
                                </div>
                            </div>
                        </div> <!--CARD FIM -->
                    </div>
                    <div class="col-sm-3 col-12">
                        <div class="bg-success top_cards">
                            <div class="row icon_margin_left">
                                <div class="col-5 icon_padd_left">
                                    <div class="float-left">
                                        <span class="fa-stack fa-sm">
                                        <i class="fa fa-circle fa-stack-2x"></i>
                                        <i class="fa fa-bitcoin fa-stack-1x fa-inverse text-success visit_icon"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="col-7 icon_padd_right">
                                    <div class="float-right cards_content">
                                        <span class="number_val">{{ $BotController->getAllCurrencys() }}</span>
                                        <br/>
                                        <span class="card_description">Moedas</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6 col-md-3 col-12">
                        <div class="bg-warning top_cards">
                            <div class="row icon_margin_left">
                                <div class="col-5 icon_padd_left">
                                    <div class="float-left">
                                        <span class="fa-stack fa-sm">
                                        <i class="fa fa-circle fa-stack-2x"></i>
                                        <i class="fa fa-dollar fa-stack-1x fa-inverse text-warning revenue_icon"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="col-7 icon_padd_right">
                                    <div class="float-right cards_content">
                                        <span class="number_val">
                                       <?php echo number_format($TransactionController->getAllTotal(), 2, ',', ' '); ?>
                                        </span>
                                        <br/>
                                        <span class="card_description">Balanço R$</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-3 col-12">
                        <div class="bg-mint top_cards">
                            <div class="row icon_margin_left">
                                <div class="col-5 icon_padd_left">
                                    <div class="float-left">
                                        <span class="fa-stack fa-sm">
                                        <i class="fa fa-circle fa-stack-2x"></i>
                                        <i class="fa fa-arrows-h  fa-stack-1x fa-inverse text-mint sub"></i>
                                        </span>
                                    </div>
                                </div>
                                <div class="col-7 icon_padd_right">
                                    <div class="float-right cards_content">
                                        <span class="number_val">
                                        {{$TransactionController->getAllTrans()}}
                                        </span>
                                        <br/>
                                        <span class="card_description">Trades</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12 col-12">
                <div class="card m-t-35">
                    <div class="card-header bg-white">
                        Meus Bots
                    </div>
                    <div class="card-block flip-scroll">
                        <button class="btn btn-raised btn-success md-trigger adv_cust_mod_btn" data-toggle="modal" data-target="#modal-newbot">Novo Bot</button>
                        <a href="{{route('bot.stopall')}}">
                            <button class="btn btn-danger">Parar Todos</button>
                        </a></br>
                        @if($errors->any())
                            {{$errors->first()}}
                        @endif
                        </br>
                        <div class="m-t-35 table-responsive">
                            <table class="table table-bordered table-striped flip-content">
                                <thead class="flip-content">
                                <tr>
                                    <th>Status</th>
                                    <th>Par</th>
                                    <th>Corretora</th>
                                    <th>Variação</th>
                                    <th>Capital</th>
                                    <th>Info.</th>
                                    <th>Estado</th>
                                    <th></th>
                                    <th></th>
                                </tr>
                                </thead>
                                <tbody>
                                @foreach($BotController->getAllBots() as $bot)
                                <tr>
                                    <td>
                                        @if($ProcessController->checkBOT($bot->id) == True)
                                        	<center>
                                            <div style="width:4px;height:0;border:5px solid #a0f441;overflow:hidden">
                                            </div>
                                            <center>
                                        @else
                                        	<center>
                                            <div style="width:4px;height:0;border:5px solid red;overflow:hidden">
                                            </div>
                                        	</center>

                                        @endif
                                    </td>
                                    <td>{{ $bot->currency }}</td>
                                    @if($bot->exchange == 'bittrex')
                                        <td><img width="15" height="15" src="img/exchanges/bittrex.png"/> Bittrex</td>
                                    @else
                                        <td><img width="15" height="15" src="img/exchanges/binance.png"/> Binance</td>
                                    @endif
                                    <td>
                                        <?php echo number_format($TransactionController->getTotal($bot->id), 2, ',', ' '); ?> BRL</td>
                                    </td>
                                    <td>
                                    {{ Form::open(['method' => 'POST', 'route' => ['bot.updatewallet', $bot->id]]) }}
                                    @if($bot->active == 1)
                                        <select name="order_value" class="form-control" onchange='this.form.submit()'>
                                            <option selected disabled>{{$bot->order_value*100}} %</option>
                                            <option value="0.1">10%</option>
                                            <option value="0.25">25%</option>
                                            <option value="0.35">35%</option>
                                            <option value="0.5">50%</option>
                                            <option value="0.75">75%</option>
                                            <option value="0.95">95%</option>
                                        </select>
                                    @elseif($BotController->getMarket($bot->id) == 'BTC')
                                        <select name="order_value" class="form-control" onchange='this.form.submit()'>
                                            <option selected disabled>{{$bot->order_value}} BTC</option>
                                            <option value="0.1">0.1 BTC</option>
                                            <option value="0.25">0.25 BTC</option>
                                            <option value="0.35">0.35 BTC</option>
                                            <option value="0.5">0.5 BTC</option>
                                            <option value="0.75">0.75 BTC</option>
                                            <option value="0.95">0.95 BTC</option>
                                        </select>
                                    @else
                                        <select name="order_value" class="form-control" onchange='this.form.submit()'>
                                            <option selected disabled>{{$bot->order_value}} USD</option>
                                            <option value="500.0">500 USD</option>
                                            <option value="1000.0">1000 USD</option>
                                            <option value="3000.0">3000 USD</option>
                                            <option value="5000.0">5000 USD</option>
                                        </select>
                                    @endif
                                    {{ Form::close() }}
                                    </td>
                                    <td>
                                        <center>
                                        <i class="fa fa-question-circle-o" data-toggle="tooltip" data-placement="top" title="" data-original-title="
                                        @if($bot->strategy_buy == 0)
                                            Contra Turtle
                                        @elseif($bot->strategy_buy == 1)
                                            Inside Bar
                                        @elseif($bot->strategy_buy == 2)
                                            Double UP
                                        @elseif($bot->strategy_buy == 4)
                                            RSI + Resistance
                                        @else
                                            Pivot UP
                                        @endif/
                                        @if($bot->strategy_sell == 0)
                                            Via Estrategia
                                        @else
                                            Lucro Fixo [{{$bot->percentage}}]
                                        @endif/Stoploss: {{$bot->stoploss*100}}%/Timeframe: {{$bot->period}}
                                        "></i>
                                        </center>
                                    </td>
                                    <td>
                                    {{ Form::open(['method' => 'GET', 'route' => ['bot.active', $bot->id]]) }}
                                        @if($bot->active == 0)
                                            <button type="submit" class="btn btn-warning"><i class="fa fa-refresh"></i> Simulando</button>
                                        @else
                                            <button type="submit" class="btn btn-success"><i class="fa fa-refresh"></i> Operando</button>
                                        @endif
                                    {{ Form::close() }}
                                    </td>
                                    <td>
                                        {{ Form::open(['method' => 'GET', 'route' => ['bot.stop', $bot->id]]) }}
                                            {{ Form::submit('Parar', ['class' => 'btn btn-danger']) }}
                                        {{ Form::close() }}
                                    </td>
                                    <td>
                                        {{ Form::open(['method' => 'DELETE', 'route' => ['bot.destroy', $bot->id]]) }}
                                            <button type="submit" class="btn btn-danger"><i class="fa fa-trash"></i></button>
                                        {{ Form::close() }}
                                    </td>
                                </tr>
                               @endforeach
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- /.outer -->
</div>
<!-- /#content -->
<!-- Modal -->
</div>
</div>

<div class="modal fade" id="modal-newbot" role="dialog" aria-labelledby="modalLabelsuccess" aria-hidden="true" style="display: none;">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header bg-success">
                <h4 class="modal-title text-white" id="modalLabelsuccess">Criar Novo Bot</h4>
            </div>
            <div class="modal-body">
                <form method="POST" action="{{ route('bot.create') }}">
                    {{ csrf_field() }}
                    <label>Corretora <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <select id="exchange" name="exchange" class="form-control" onchange="getMarkets()">
                        <option value="bittrex">Bittrex</option>
                        <option value="binance">Binance</option>
                    </select>
                    </br><label>Mercado <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <input id="currencys" type="text" name="currency" class="dropdown-input"/>
                    <button class="dropdown-btn" type="button"><span class="caret"></span></button>
                    </br>
                    </br><label>Tempo Gráfico</label>
                    <select name="period" class="form-control">
                        <option value="Day">1 dia</option>
                        <option value="hour">1 hora</option>
                        <option value="thirtyMin">30 minutos</option>
                    </select>
                    </br><label>Estrategia de Compra <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <select name="strategy_buy" class="form-control">
                        <option value="0">Contra Turtle</option>
                        <option value="1">Inside Bar</option>
                        <option value="2">Double UP</option>
                        <option value="3">Pivot UP</option>
                        <option value="4">RSI Resistance</option>
                    </select>
                    </br><label>Estrategia de Venda <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <select name="strategy_sell" class="form-control">
                        <option value="0">Via Estrategia</option>
                        <option value="1">Lucro Fixo (preco compra + lucro)</option>
                    </select>
                    </br><label>Lucro Fixo % <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <select name="percentage" class="form-control">
                        <option value="0.01">1%</option>
                        <option value="0.015">1.5%</option>
                        <option value="0.02">2%</option>
                        <option value="0.03">3%</option>
                        <option value="0.05">5%</option>
                        <option value="0.07">7%</option>
                        <option value="0.10">10%</option>
                    </select>
                    </br><label>Parar Perda % <i  data-toggle="tooltip" data-placement="top" title="Hooray!" class="fa fa-question-circle-o" style='color:#00cc99'></i></label></br>
                    <select name="stoploss" class="form-control">
                        <option value="0.01">1%</option>
                        <option value="0.015">1.5%</option>
                        <option value="0.02">2%</option>
                        <option value="0.03">3%</option>
                        <option value="0.05">5%</option>
                        <option value="0.07">7%</option>
                        <option value="0.1">10%</option>
                        <option value="0.15">15%</option>
                        <option value="0.2">20%</option>
                        <option value="0.25">25%</option>
                        <option value="0.5">50%</option>
                        <option value="0.75">75%</option>
                    </select>
                    </br></br>
                    <button type="submit" class="btn btn-success">Criar</button>
                    </br></br>
                </form>
            </div>
            <div class="modal-footer">
                <button class="btn  btn-success" data-dismiss="modal">Sair</button>
            </div>
        </div>
    </div>
</div>


<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
<script src="http://198.50.194.124/js/awesomplete.js"></script>
<script type="text/javascript">
    function getMarkets() {
        let exchange = document.getElementById("exchange").value;
        let markets = [];
        if(exchange == 'binance') {
            console.log("sou binance eo")
            markets = ['USDT-BTC', 'USDT-ETH', 'USDT-BNB', 'USDT-BCC', 'USDT-NEO', 'USDT-LTC', 'USDT-QTUM', 'BTC-ETH', 'BTC-LTC', 'BTC-BNB', 'BTC-NEO', 'BTC-BCC', 'BTC-GAS', 'BTC-HSR', 'BTC-MCO', 'BTC-WTC', 'BTC-LRC', 'BTC-QTUM', 'BTC-YOYO', 'BTC-OMG', 'BTC-ZRX', 'BTC-STRAT', 'BTC-SNGLS', 'BTC-BQX', 'BTC-KNC', 'BTC-FUN', 'BTC-SNM', 'BTC-IOTA', 'BTC-LINK', 'BTC-XVG', 'BTC-SALT', 'BTC-MDA', 'BTC-MTL', 'BTC-SUB', 'BTC-EOS', 'BTC-SNT', 'BTC-ETC', 'BTC-MTH', 'BTC-ENG', 'BTC-DNT', 'BTC-ZEC', 'BTC-BNT', 'BTC-AST', 'BTC-DASH', 'BTC-OAX', 'BTC-ICN', 'BTC-BTG', 'BTC-EVX', 'BTC-REQ', 'BTC-VIB', 'BTC-TRX', 'BTC-POWR', 'BTC-ARK', 'BTC-XRP', 'BTC-MOD', 'BTC-ENJ', 'BTC-STORJ', 'BTC-VEN', 'BTC-KMD', 'BTC-RCN', 'BTC-NULS', 'BTC-RDN', 'BTC-XMR', 'BTC-DLT', 'BTC-AMB', 'BTC-BAT', 'BTC-BCPT', 'BTC-ARN', 'BTC-GVT', 'BTC-CDT', 'BTC-GXS', 'BTC-POE', 'BTC-QSP', 'BTC-BTS', 'BTC-XZC', 'BTC-LSK', 'BTC-TNT', 'BTC-FUEL', 'BTC-MANA', 'BTC-BCD', 'BTC-DGD', 'BTC-ADX', 'BTC-ADA', 'BTC-PPT', 'BTC-CMT', 'BTC-XLM', 'BTC-CND', 'BTC-LEND', 'BTC-WABI', 'BTC-TNB', 'BTC-WAVES', 'BTC-GTO', 'BTC-ICX', 'BTC-OST', 'BTC-ELF', 'BTC-AION', 'BTC-NEBL', 'BTC-BRD', 'BTC-EDO', 'BTC-WINGS', 'BTC-NAV', 'BTC-LUN', 'BTC-TRIG', 'BTC-APPC', 'BTC-VIBE', 'BTC-RLC', 'BTC-INS', 'BTC-PIVX', 'BTC-IOST', 'BTC-CHAT', 'BTC-STEEM', 'BTC-NANO', 'BTC-VIA', 'BTC-BLZ', 'BTC-AE', 'BTC-RPX', 'BTC-NCASH', 'BTC-POA', 'BTC-ZIL', 'BTC-ONT', 'BTC-STORM', 'BTC-XEM', 'BTC-WAN', 'BTC-WPR', 'BTC-QLC', 'BTC-SYS', 'BTC-GRS']; 
        }
        if(exchange == 'bittrex') {
            console.log("sou bittrex eo")
            markets = ['BTC-2GIVE','BTC-ABY','BTC-ADA','BTC-ADT','BTC-ADX','BTC-AEON','BTC-AMP','BTC-ANT','BTC-ARDR','BTC-ARK','BTC-AUR','BTC-BAT','BTC-BAY','BTC-BCC','BTC-BCPT','BTC-BCY','BTC-BITB','BTC-BLITZ','BTC-BLK','BTC-BLOCK','BTC-BNT','BTC-BRK','BTC-BRX','BTC-BSD','BTC-BTG','BTC-BURST','BTC-BYC','BTC-CANN','BTC-CFI','BTC-CLAM','BTC-CLOAK','BTC-COVAL','BTC-CRB','BTC-CRW','BTC-CURE','BTC-CVC','BTC-DASH','BTC-DCR','BTC-DCT','BTC-DGB','BTC-DMD','BTC-DMT','BTC-DNT','BTC-DOGE','BTC-DOPE','BTC-DTB','BTC-DYN','BTC-EBST','BTC-EDG','BTC-EFL','BTC-EGC','BTC-EMC','BTC-EMC2','BTC-ENG','BTC-ENRG','BTC-ERC','BTC-ETC','BTC-ETH','BTC-EXCL','BTC-EXP','BTC-FCT','BTC-FLDC','BTC-FLO','BTC-FTC','BTC-GAM','BTC-GAME','BTC-GBG','BTC-GBYTE','BTC-GEO','BTC-GLD','BTC-GNO','BTC-GNT','BTC-GOLOS','BTC-GRC','BTC-GRS','BTC-GUP','BTC-HMQ','BTC-IGNIS','BTC-INCNT','BTC-IOC','BTC-ION','BTC-IOP','BTC-KMD','BTC-KORE','BTC-LBC','BTC-LGD','BTC-LMC','BTC-LRC','BTC-LSK','BTC-LTC','BTC-LUN','BTC-MANA','BTC-MCO','BTC-MEME','BTC-MER','BTC-MLN','BTC-MONA','BTC-MUE','BTC-MUSIC','BTC-NAV','BTC-NBT','BTC-NEO','BTC-NEOS','BTC-NLG','BTC-NMR','BTC-NXC','BTC-NXS','BTC-NXT','BTC-OK','BTC-OMG','BTC-OMNI','BTC-PART','BTC-PAY','BTC-PINK','BTC-PIVX','BTC-PKB','BTC-POT','BTC-POWR','BTC-PPC','BTC-PTC','BTC-PTOY','BTC-QRL','BTC-QTUM','BTC-QWARK','BTC-RADS','BTC-RBY','BTC-RCN','BTC-RDD','BTC-REP','BTC-RLC','BTC-RVR','BTC-SALT','BTC-SBD','BTC-SC','BTC-SEQ','BTC-SHIFT','BTC-SIB','BTC-SLR','BTC-SLS','BTC-SNRG','BTC-SNT','BTC-SPHR','BTC-SPR','BTC-SRN','BTC-STEEM','BTC-STORJ','BTC-STRAT','BTC-SWIFT','BTC-SWT','BTC-SYNX','BTC-SYS','BTC-THC','BTC-TIX','BTC-TKS','BTC-TRST','BTC-TRUST','BTC-TRX','BTC-TUSD','BTC-TX','BTC-UBQ','BTC-UKG','BTC-UNB','BTC-UP','BTC-VEE','BTC-VIA','BTC-VIB','BTC-VRC','BTC-VRM','BTC-VTC','BTC-VTR','BTC-WAVES','BTC-WAX','BTC-WINGS','BTC-XCP','BTC-XDN','BTC-XEL','BTC-XEM','BTC-XLM','BTC-XMG','BTC-XMR','BTC-XMY','BTC-XRP','BTC-XST','BTC-XVC','BTC-XVG','BTC-XWC','BTC-XZC','BTC-ZCL','BTC-ZEC','BTC-ZEN','BTC-ZRX','USDT-ADA','USDT-BCC','USDT-BTC','USDT-BTG','USDT-DASH','USDT-ETC','USDT-ETH','USDT-LTC','USDT-NEO','USDT-NXT','USDT-OMG','USDT-TUSD','USDT-XMR','USDT-XRP','USDT-XVG','USDT-ZEC'];
        }
        console.log(exchange);
        console.log(markets);
        var comboplete = new Awesomplete('input.dropdown-input', {
            list: markets,
            minChars: 0,
        });
        Awesomplete.$('.dropdown-btn').addEventListener("click", function() {
            if (comboplete.ul.childNodes.length === 0) {
                comboplete.minChars = 0;
                comboplete.evaluate();
            }
            else if (comboplete.ul.hasAttribute('hidden')) {
                comboplete.open();
            }
            else {
                comboplete.close();
            }
        });
    };
    </script>
@stop
<!-- /#wrap -->
