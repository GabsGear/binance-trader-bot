@inject('BotController', 'App\Http\Controllers\BotController')
@inject('TransactionController', 'App\Http\Controllers\TransactionController')
@inject('ProcessController', 'App\Http\Controllers\ProcessController')
@inject('UserController', 'App\Http\Controllers\UserController')
@inject('User', 'App\User')
<?php $user = $UserController->getUser(); ?>

@extends('layouts/default')
@section('content')

<link rel="stylesheet" type="text/css" href="css/pages/widgets.css">
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
                    <div class="col-12 col-sm-6 col-lg-3">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-android text-success" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count5">{{$BotController->countBots(1)}}</h3>
                                <p>Bots Ativos</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3 media_max_573">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-bitcoin text-danger" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count6">{{ $BotController->getAllCurrencys() }}</h3>
                                <p>Moedas</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3 media_max_991">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-money text-primary" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count7">
                                    R$ {{ number_format($TransactionController->getBalanceTotal(), 2, '.', ' ') }}
                                </h3>
                                <p>Balanço Total</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3 media_max_991">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <img src="img/exchanges/binance.png">
                            </div>
                            <div class="text-right">
                                <h4 id="widget_count8">Binance</h4>
                                @if($UserController->check_binance() == 1)
                                    <p id="bin_balance">Carregando...</p>
                                @else
                                    <p>Não conectado...</p>
                                @endif
                            </div>
                        </div>
                    </div>
                </div> <!---FIM ROW-->
                </br>
                <div class="row">
                    <div class="col-12 col-sm-6 col-lg-3">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-arrows-h text-warning" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count5">{{$TransactionController->count(1)}}</h3>
                                <p>Trades Fechados</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3 media_max_573">
                        <div class="widget_icon_bgclr icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-arrows-h text-info" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count6">{{$TransactionController->count(0)}}</h3>
                                <p>Trades Abertos</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <i class="fa fa-star-o" aria-hidden="true"></i>
                            </div>
                            <div class="text-right">
                            <?php $date = explode('-', $UserController->getUser()->expire_date) ?>
                                @if($user->premium == 1 and $UserController->checkPremium() == true)
                                    <h3 id="widget_count5">Plano <font color="#c0c0c0"><b>Prata</b></font></h3>
                                    <a href="{{route('payment.view')}}"><p> <i class="fa fa-refresh" aria-hidden="true"></i> RENOVAR</a> | 
                                    Expira {{$date[2]}}/{{$date[1]}}</p>
                                @elseif($user->premium == 2 and $UserController->checkPremium() == true)
                                    <h3 id="widget_count5">Plano <font color="#cd7f32"><b>Ouro</b></font></h3>
                                    <a href="{{route('payment.view')}}"><p> <i class="fa fa-refresh" aria-hidden="true"></i> RENOVAR</a> | 
                                    Expira {{$date[2]}}/{{$date[1]}}</p>
                                @else
                                    <h3 id="widget_count5">Plano <font color="#cd7f32"><b>Bronze</b></font></h3>
                                    <a href="{{route('payment.view')}}"><p> <i class="fa fa-refresh" aria-hidden="true"></i> CONTRATAR</a></p>
                                @endif
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3 media_max_991">
                        <div class="icon_align bg-white section_border">
                            <div class="float-left progress_icon">
                                <img src="img/exchanges/bittrex.png">
                            </div>
                            <div class="text-right">
                                <h3 id="widget_count8">Bittrex</h3>
                                @if($UserController->check_bittrex() == 1)
                                    <p id="bit_balance">Carregando...</p>
                                @else
                                    <p>Não conectado...</p>
                                @endif
                            </div>
                        </div>
                    </div>
                </div> <!---FIM ROW-->
            </div>
        </div> <!---FIM ROW-->
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
                                    <th>ID</th>
                                    <th>Mercado&Moeda</th>
                                    <th>Corretora</th>
                                    <th>Variação</th>
                                    <th>Capital</th>
                                    <th>Info.</th>
                                    <th>Estado</th>
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
                                    <td>{{ $bot->name }}</td>
                                    <td>{{ $bot->currency }}</td>
                                    @if($bot->exchange == 'bittrex')
                                        <td><img width="15" height="15" src="img/exchanges/bittrex.png"/> Bittrex</td>
                                    @else
                                        <td><img width="15" height="15" src="img/exchanges/binance.png"/> Binance</td>
                                    @endif
                                    <td>
                                        {{ number_format($TransactionController->getBalance($bot->id), 2, '.', ' ') }} BRL</td>
                                    </td>
                                    <td>
                                    {{ Form::open(['method' => 'POST', 'route' => ['bot.updatewallet', $bot->id]]) }}
                                    @if($bot->active == 1)
                                        <select name="order_value" class="form-control" onchange='this.form.submit()'>
                                            <option selected disabled>{{$bot->order_value*100}} %</option>
                                            <option value="0.05">5%</option>
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
                                        @endif
                                        /Lucro:{{$bot->percentage*100}}%
                                        /Stoploss: {{$bot->stoploss*100}}%/Timeframe: {{$bot->period}}
                                        /Ordem mínima: R${{ $bot->min_order }}
                                        "></i>
                                        </center>
                                    </td>
                                    <td>
                                    {{ Form::open(['method' => 'POST', 'route' => ['bot.active']]) }}
                                        <select name="active" class="form-control" onchange='this.form.submit()'>
                                            @if($bot->active == 0)
                                                <option selected disabled>Simulando</option>
                                            @elseif($bot->active == 1)
                                                <option selected disabled>Operando</option>
                                            @else
                                                <option selected disabled>Parado</option>
                                            @endif
                                            <option value="0">Simular</option>
                                            <option value="1">Operar</option>
                                            <option value="2">Parar</option>
                                        </select>
                                        <input type="hidden" name="id" value="{{ $bot->id }}">
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
    <div class="modal-dialog  modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header bg-success">
                <h4 class="modal-title text-white" id="modalLabelsuccess">Criar Novo Bot</h4>
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-md-6">
                        <form method="POST" action="{{ route('bot.create') }}">
                        {{ csrf_field() }}
                        <label><i  data-toggle="tooltip" data-placement="right" title="Qual corretora o robô ira operar." class="fa fa-question-circle-o" style='color:#00cc99'></i>
                        Corretora </label></br>
                        <select id="exchange" name="exchange" class="form-control" onchange="getMarkets()">
                            <option value="bittrex">Bittrex</option>
                            <option value="binance">Binance</option>
                        </select>
                        </br><label><i data-toggle="tooltip" data-placement="right" title="Digite a sigla oficial da moeda por exemplo Litecoin é LTC." class="fa fa-question-circle-o" style='color:#00cc99'></i>
                        Mercado & Moeda </label></br>
                        <input id="currencys" type="text" name="currency" class="dropdown-input"/>
                        <button type="button" id="drop" class="btn btn-light dropdown-toggle b-r-0" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        </button>
                        </br>
                        </br><label><i data-toggle="tooltip" data-placement="right" title="Tempo dos candlesticks que serão analisados." class="fa fa-question-circle-o" style='color:#00cc99'></i></label>
                        Tempo Gráfico </br>
                        </label>
                        <select name="period" class="form-control">
                            <option value="Day">1 dia</option>
                            <option value="hour">1 hora</option>
                            <option value="thirtyMin">30 minutos</option>
                        </select>
                        </br><label><i data-toggle="tooltip" data-placement="right" title="Defina um valor mínimo em reais para abrir uma ordem de compra." class="fa fa-question-circle-o" style='color:#00cc99'></i></label>
                        Ordem Mínima </br>
                        </label>
                        <select name="min_order" class="form-control">
                            <option value="50">R$50.00</option>
                            <option value="100">R$100.00</option>
                            <option value="200">R$200.00</option>
                            <option value="300">R$300.00</option>
                            <option value="500">R$500.00</option>
                            <option value="1000">R$1000.00</option>
                            <option value="2000">R$2000.00</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label><i  data-toggle="tooltip" data-placement="right" title="Detalhes sobre cada uma das estratégias de compra estão em nosso blog." class="fa fa-question-circle-o" style='color:#00cc99'></i>
                        Estratégia de Compra </label></br>
                        <select name="strategy_buy" class="form-control">
                            <option value="0">Contra Turtle</option>
                            <option value="1">Inside Bar</option>
                            <option value="2">Double UP</option>
                            <option value="3">Pivot UP</option>
                            <option value="4">RSI Resistance</option>
                        </select>
                        </br><label><i  data-toggle="tooltip" data-placement="right" title="Defina o lucro a ser atingido quando uma compra for efetuada." class="fa fa-question-circle-o" style='color:#00cc99'></i> 
                        Porcentagem de Lucro </label></br>
                        <select name="percentage" class="form-control">
                            <option value="0.01">1%</option>
                            <option value="0.015">1.5%</option>
                            <option value="0.02">2%</option>
                            <option value="0.03">3%</option>
                            <option value="0.05">5%</option>
                            <option value="0.07">7%</option>
                            <option value="0.10">10%</option>
                        </select>
                        </br><label><i  data-toggle="tooltip" data-placement="right" title="Proteja seu capital definindo um limite de perda em porcentagem." class="fa fa-question-circle-o" style='color:#00cc99'></i>
                        Parar Perda % </label></br>
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
                        </br><label><i data-toggle="tooltip" data-placement="right" title="Defina que modo o seu bot irá iniciar." class="fa fa-question-circle-o" style='color:#00cc99'></i></label>
                        Modo </br>
                        </label>
                        <select name="active" class="form-control">
                            <option value="2">Parado</option>
                            <option value="0">Simulação</option>
                            <option value="1">Operação</option>
                        </select>
                    </div> <!--FIM MD6 -->
                </div> <!--FIM ARROW -->
            </div>
            <div class="modal-footer">
                    <button type="button" data-dismiss="modal" class="btn btn-light">Sair</button>
                    <button class="btn  btn-success">Criar</button>
                </form>
            </div>
        </div>
    </div>
</div>


<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
<script src="http://painel.protraderbot.com/js/awesomplete.js"></script>
<script type="text/javascript">
    let markets = ['BTC-2GIVE', 'BTC-ABY', 'BTC-ADA', 'BTC-ADT', 'BTC-ADX', 'BTC-AEON', 'BTC-AMP', 'BTC-ANT', 'BTC-ARDR', 'BTC-ARK', 'BTC-AUR', 'BTC-BAT', 'BTC-BAY', 'BTC-BCC', 'BTC-BCPT', 'BTC-BCY', 'BTC-BITB', 'BTC-BLITZ', 'BTC-BLK', 'BTC-BLOCK', 'BTC-BNT', 'BTC-BRK', 'BTC-BRX', 'BTC-BSD', 'BTC-BTG', 'BTC-BURST', 'BTC-BYC', 'BTC-CANN', 'BTC-CFI', 'BTC-CLAM', 'BTC-CLOAK', 'BTC-COVAL', 'BTC-CRB', 'BTC-CRW', 'BTC-CURE', 'BTC-CVC', 'BTC-DASH', 'BTC-DCR', 'BTC-DCT', 'BTC-DGB', 'BTC-DMD', 'BTC-DMT', 'BTC-DNT', 'BTC-DOGE', 'BTC-DOPE', 'BTC-DTB', 'BTC-DYN', 'BTC-EBST', 'BTC-EDG', 'BTC-EFL', 'BTC-EGC', 'BTC-EMC', 'BTC-EMC2', 'BTC-ENG', 'BTC-ENRG', 'BTC-ERC', 'BTC-ETC', 'BTC-ETH', 'BTC-EXCL', 'BTC-EXP', 'BTC-FCT', 'BTC-FLDC', 'BTC-FLO', 'BTC-FTC', 'BTC-GAM', 'BTC-GAME', 'BTC-GBG', 'BTC-GBYTE', 'BTC-GEO', 'BTC-GLD', 'BTC-GNO', 'BTC-GNT', 'BTC-GOLOS', 'BTC-GRC', 'BTC-GRS', 'BTC-GUP', 'BTC-HMQ', 'BTC-IGNIS', 'BTC-INCNT', 'BTC-IOC', 'BTC-ION', 'BTC-IOP', 'BTC-KMD', 'BTC-KORE', 'BTC-LBC', 'BTC-LGD', 'BTC-LMC', 'BTC-LRC', 'BTC-LSK', 'BTC-LTC', 'BTC-LUN', 'BTC-MANA', 'BTC-MCO', 'BTC-MEME', 'BTC-MER', 'BTC-MLN', 'BTC-MONA', 'BTC-MUE', 'BTC-MUSIC', 'BTC-NAV', 'BTC-NBT', 'BTC-NEO', 'BTC-NEOS', 'BTC-NLG', 'BTC-NMR', 'BTC-NXC', 'BTC-NXS', 'BTC-NXT', 'BTC-OK', 'BTC-OMG', 'BTC-OMNI', 'BTC-PART', 'BTC-PAY', 'BTC-PINK', 'BTC-PIVX', 'BTC-PKB', 'BTC-POT', 'BTC-POWR', 'BTC-PPC', 'BTC-PTC', 'BTC-PTOY', 'BTC-QRL', 'BTC-QTUM', 'BTC-QWARK', 'BTC-RADS', 'BTC-RBY', 'BTC-RCN', 'BTC-RDD', 'BTC-REP', 'BTC-RLC', 'BTC-RVR', 'BTC-SALT', 'BTC-SBD', 'BTC-SC', 'BTC-SEQ', 'BTC-SHIFT', 'BTC-SIB', 'BTC-SLR', 'BTC-SLS', 'BTC-SNRG', 'BTC-SNT', 'BTC-SPHR', 'BTC-SPR', 'BTC-SRN', 'BTC-STEEM', 'BTC-STORJ', 'BTC-STRAT', 'BTC-SWIFT', 'BTC-SWT', 'BTC-SYNX', 'BTC-SYS', 'BTC-THC', 'BTC-TIX', 'BTC-TKS', 'BTC-TRST', 'BTC-TRUST', 'BTC-TRX', 'BTC-TUSD', 'BTC-TX', 'BTC-UBQ', 'BTC-UKG', 'BTC-UNB', 'BTC-UP', 'BTC-VEE', 'BTC-VIA', 'BTC-VIB', 'BTC-VRC', 'BTC-VRM', 'BTC-VTC', 'BTC-VTR', 'BTC-WAVES', 'BTC-WAX', 'BTC-WINGS', 'BTC-XCP', 'BTC-XDN', 'BTC-XEL', 'BTC-XEM', 'BTC-XLM', 'BTC-XMG', 'BTC-XMR', 'BTC-XMY', 'BTC-XRP', 'BTC-XST', 'BTC-XVC', 'BTC-XVG', 'BTC-XWC', 'BTC-XZC', 'BTC-ZCL', 'BTC-ZEC', 'BTC-ZEN', 'BTC-ZRX', 'USDT-ADA', 'USDT-BCC', 'USDT-BTC', 'USDT-BTG', 'USDT-DASH', 'USDT-ETC', 'USDT-ETH', 'USDT-LTC', 'USDT-NEO', 'USDT-NXT', 'USDT-OMG', 'USDT-TUSD', 'USDT-XMR', 'USDT-XRP', 'USDT-XVG', 'USDT-ZEC', 'USDT-BNB', 'USDT-QTUM', 'BTC-BNB', 'BTC-GAS', 'BTC-HSR', 'BTC-WTC', 'BTC-YOYO', 'BTC-SNGLS', 'BTC-BQX', 'BTC-KNC', 'BTC-FUN', 'BTC-SNM', 'BTC-IOTA', 'BTC-LINK', 'BTC-MDA', 'BTC-MTL', 'BTC-SUB', 'BTC-EOS', 'BTC-MTH', 'BTC-AST', 'BTC-OAX', 'BTC-ICN', 'BTC-EVX', 'BTC-REQ', 'BTC-MOD', 'BTC-ENJ', 'BTC-VEN', 'BTC-NULS', 'BTC-RDN', 'BTC-DLT', 'BTC-AMB', 'BTC-ARN', 'BTC-GVT', 'BTC-CDT', 'BTC-GXS', 'BTC-POE', 'BTC-QSP', 'BTC-BTS', 'BTC-TNT', 'BTC-FUEL', 'BTC-BCD', 'BTC-DGD', 'BTC-PPT', 'BTC-CMT', 'BTC-CND', 'BTC-LEND', 'BTC-WABI', 'BTC-TNB', 'BTC-GTO', 'BTC-ICX', 'BTC-OST', 'BTC-ELF', 'BTC-AION', 'BTC-NEBL', 'BTC-BRD', 'BTC-EDO', 'BTC-TRIG', 'BTC-APPC', 'BTC-VIBE', 'BTC-INS', 'BTC-IOST', 'BTC-CHAT', 'BTC-NANO', 'BTC-BLZ', 'BTC-AE', 'BTC-RPX', 'BTC-NCASH', 'BTC-POA', 'BTC-ZIL', 'BTC-ONT', 'BTC-STORM', 'BTC-WAN', 'BTC-WPR', 'BTC-QLC'];
    var comboplete = new Awesomplete('input.dropdown-input', {
        list: markets,
        minChars: 0,
    });
    Awesomplete.$('#drop').addEventListener("click", function() {
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

    let bin_btc = 0;
    let bin_usd = 0;
    let bit_btc = 0;
    let bit_usd = 0;

    $.get("http://198.50.194.124/balance/binance/BTC", function(bin_btc) {
        return bin_btc;
    }).then(function(bin_btc) {
        $.getJSON("http://198.50.194.124/balance/binance/USDT", function(bin_usd) {
            $("#bin_balance").html(bin_usd+" <b>USD</b>|"+bin_btc+" <b>BTC</b>");
        });
    });

    $.get("http://198.50.194.124/balance/bittrex/BTC", function(bit_btc) {
        return bit_btc;
    }).then(function(bit_btc) {
        $.getJSON("http://198.50.194.124/balance/bittrex/USDT", function(bit_usd) {
            $("#bit_balance").html(bit_usd+" <b>USD</b>|"+bit_btc+" <b>BTC</b>");
        });
    });

</script>
@stop
<!-- /#wrap -->
