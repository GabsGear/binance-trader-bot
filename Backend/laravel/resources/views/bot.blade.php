@inject('ProcessController', 'App\Http\Controllers\ProcessController')
@inject('BotController', 'App\Http\Controllers\BotController')
@inject('TransController', 'App\Http\Controllers\TransactionController')
@inject('ChartController', 'App\Http\Controllers\ChartController')

@extends('layouts/default')
@section('content')

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript">
    function getConsole() {
        var full_url = document.URL;
        var url_array = full_url.split('/');
        var bot_id = url_array[url_array.length-1];
        var ip = url_array[2];
        $.get("http://"+ip+"/bot/console/"+bot_id+"", function(data) {
            $("#console").html(data);
        });
    }

    getConsole()
    setInterval(getConsole, 300)
</script>
<header class="head">
<div class="main-bar">
   <div class="row no-gutters">
       <div class="col-12">
           <h4 class="m-t-5">
               <i class="fa fa-android"></i>
               Bot ID: {{$bot->id}} | Par de Operacao: {{$bot->currency}} | Rodando em modo:
                    @if($bot->active == 1)
                        Operando
                    @else
                        Simulação
                    @endif
           </h4>
       </div>
   </div>
</div>
</header>
<div class="outer">
    <div class="inner bg-container">
    <div class="row">
        <div class="col-sm-6 col-12">
            <div class="card m-t-35">
                <div class="card-header bg-white">
                    Estratégias de Operação
                </div>
                <div class="card-block">
                    <div class="alert alert-success alert-dismissable">
                        <h4 class="text-white">Estratégia de Compra</h4>
                        <form method="POST" action="{{route('bot.update', $bot->id)}}">
                            {{ csrf_field() }}
                            <label>Forma de Compra</label>
                            <select name="strategy_buy" class="form-control">
                                <option value="{{$bot->strategy_buy}}">
                                    @switch($bot->strategy_buy)
                                        @case(0)
                                            Atual: Contra Turtle (Volatilidade)
                                        @break
                                    @endswitch
                                </option>
                                <option value="0">Contra Turtle (Volatilidade)</option>
                            </select>
                        </br>
                    </div>
                    <div class="alert alert-danger alert-dismissable">
                    <h4 class="text-white">Estratégia de Venda</h4>
                    	<label>Forma de Venda</label>
                    	<select name="strategy_sell" class="form-control">
	                        <option value="{{$bot->strategy_sell}}">
                                @switch($bot->strategy_sell)
                                    @case(0)
                                        Atual: Via Estrategia
                                    @break
                                    @case(1)
                                        Atual: Lucro Fixo (preco compra + lucro)
                                    @break
                                @endswitch
                            </option>
	                        <option value="0">Via Estrategia</option>
                            <option value="1">Lucro Fixo (preco compra + lucro)</option>
	                    </select>
                    	<label>Porcentagem de Lucro Fixo (somente se a forma de venda for por lucro fixo)</label>
	                    <select name="percentage" class="form-control">
	                        <option value="0.01">1%</option>
	                        <option value="0.01">1.5%</option>
	                        <option value="0.02">2%</option>
	                        <option value="0.03">3%</option>
	                        <option value="0.05">5%</option>
	                        <option value="0.07">7%</option>
	                        <option value="0.10">10%</option>
	                    </select>
	                    <label>Parar Perca (padrao:10%)</label>
	                    <select name="stoploss" class="form-control">
	                        <option value="0.05">5%</option>
	                        <option value="0.07">7%</option>
	                        <option value="0.1">10%</option>
	                        <option value="0.15">15%</option>
	                        <option value="0.2">20%</option>
	                        <option value="0.25">25%</option>
	                        <option value="0.5">50%</option>
                             <option value="0.75">75%</option>
	                    </select>

                    </div>
                    	<button type="submit" class="btn btn-secondary">Salvar</button>
                    	</form>
                </div>
            </div>
            <div class="card m-t-35">
                <div class="card-header bg-white">
                    Carteira
                </div>
                <div class="col-lg-12">
                <p>Por padrão cada bot realiza apenas 1 ordem de compra e aguarda até que ela seja processada.</p>
                </div>
                <div class="col-lg-8 input_field_sections">
                        <form method="POST" action="{{ route('bot.updatewallet', $bot) }}">
                            {{ csrf_field() }}
                            @if($bot->active == 1)
                                <label>Porcentagem do seu saldo em carteira</label>
                                <select name="order_value" class="form-control">
                                    <option>Selecione</option>
                                    <option value="0.1">10%</option>
                                    <option value="0.25">25%</option>
                                    <option value="0.35">35%</option>
                                    <option value="0.5">50%</option>
                                    <option value="0.75">75%</option>
                                    <option value="0.95">95%</option>
                                </select>
                            @else
                                <label>Quantidade para lançar Ordem de Compra (BTC)</label>
                                <input type="text" name="order_value" value="{{$bot->order_value}}"/>
                            @endif
                            </br>
                            @if($bot->active == 1)
                                Saldo disponível: 

                            @endif
                            </br>
                            <button type="submit" class="btn btn-secondary">Salvar</button>
                            </br>
                            @if($bot->active == 1)
                                Para que o bot funcione corretamente 5% do saldo deve ficar a salvo.
                            @endif
                            </br>
                        </form>
                    </div>
            </div>
        </div>
        <div class="col-sm-6 col-12">
            <div class="card m-t-35">
                <div class="card-header bg-white">
                    Logs
                </div>
                <div class="card-block">
                    <div class="table-responsive m-t-35">
                        <table class="table" style="background:#eceeef;">
                            <tr style="border:1px solid #CCCCCC;">
                                <td width="25%">Total de trades</td>
                                <td>{{ $TransController->getTotalTrades($bot->id) }}</td>
                            </tr>
                            <tr style="border:1px solid #CCCCCC;">
                                <td width="25%">Lucro</td>
                                <td>
                                <?php echo number_format($TransController->getTotal($bot->id), 2, ',', ' '); ?> BRL</td>
                            </tr>
                            <tr>
                                
                            </tr>
                        </table>
                    </div>
                    <div class="table-responsive m-t-35">
                        <h5>Console - Tempo Real</h5>
                        <div id="console" style="margin-bottom:10px; border:2px solid #CCCCCC;">
                        </div>
                    </div>
                    <div class="alert alert-warning alert-dismissable">
                        <h4 class="text-white">Modo de Operação</h4>
                        <p>
                            Seu bot atualmente está rodando no modo
                            <?php 
                            switch ($bot->active) {
                                case 0:
                                    echo "<a class=\"alert-link\">de simulação</a>";
                                break;
                                case 1:
                                    echo "<a class=\"alert-link\">real</a>";
                                break;
                            }?>

                            , para alternar entre os modos (simulação/real) aperte o botão abaixo.
                        </p>
                        <p>
                            <a class="btn btn-secondary" href="{{route('bot.active', $bot)}}">Alternar Modo</a>
                            ou mantenha
                        </p>
                    </div>
                    <div class="alert alert-info alert-dismissable">
                        <h4 class="text-white">Tempo Gráfico</h4>
                        <p>
                            Seu bot atualmente está rodando com um tempo gráfico de 
                            <a class=\"alert-link\">{{$bot->period}}</a>.
                        </p>
                        <p>
                        <div class="col-sm-6 col-6">
                            <form method="POST" action="{{route('bot.period', $bot->id)}}">
                                {{ csrf_field() }}
                                <select name="period" class="form-control">
                                    <option value="{{$bot->period}}">Selecione</option>
                                    <option value="Day">1 dia</option>
                                    <option value="hour">1 hora</option>
                                    <option value="thirtyMin">30 minutos</option>
                                    <option value="thirtyMin">30 minutos</option>
                                </select>
                        </p>
                        <p>
                                <button type="submit" class="btn btn-secondary">Salvar</button>
                            </form>
                        </div>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-12 col-12">
            <div class="card m-t-35">
                <div class="card-header bg-white">
                    <div class="table-responsive m-t-35">
                        <h5>Histórico de Trades</h5>
                        <table class="table">
                            <thead>
                            <tr>
                                <th><font size="2px">VALOR COMPRA</font></th>
                                <th><font size="2px">VALOR VENDA</font></th>
                                <th><font size="2px">QUANTIA</font></th>
                                <th><font size="2px">LUCRO (BTC)</font></th>
                                <th><font size="2px">LUCRO (%)</font></th>
                                <th><font size="2px">DATA-ABERTURA</font></th>
                                <th><font size="2px">DATA-FECHAMENTO</font></th>
                            </tr>
                            </thead>
                            <?php  $total = 0; ?>
                            <tbody>
                            @foreach($BotController->getAllBotTransactions($bot->id) as $trans)
                            <tr>
                                <td><?php echo number_format($trans->buy_value, 8, ',', ' '); ?></td>
                                @if($trans->selled == 0)
                                    <td>ABERTA</td>
                                    <td><?php echo number_format($trans->quantity, 8, ',', ' '); ?></td>
                                    <td>ABERTA</td>
                                @else
                                    <td><?php echo number_format($trans->sell_value, 8, ',', ' '); ?></td>
                                    <td><?php echo number_format($trans->quantity, 8, ',', ' '); ?></td>
                                    <td><?php echo number_format(($trans->sell_value-$trans->buy_value)*$trans->quantity, 8, ',', ' '); ?> BTC
                                    </td>
                                @endif
                                @if($trans->selled == 1)
                                    <td> 
                                        <?php echo number_format($TransController->getPercentage($trans->sell_value, $trans->buy_value), 2, ',', ' '); ?>%  
                                    </td>
                                @else
                                    <td>--</td>
                                @endif
                                    <td>{{$trans->date_open}}</td>
                                    <td>{{$trans->date_close}}</td>
                            @endforeach
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div> <!--END ROW-->
@stop
@section('footer_scripts')
<!-- global scripts-->
<script type="text/javascript" src="js/components.js"></script>
<script type="text/javascript" src="js/custom.js"></script>
<!-- global scripts end-->
<script type="text/javascript" src="vendors/slimscroll/js/jquery.slimscroll.min.js"></script>
<script type="text/javascript" src="vendors/raphael/js/raphael-min.js"></script>
<script type="text/javascript" src="vendors/d3/js/d3.min.js"></script>
<script type="text/javascript" src="vendors/c3/js/c3.min.js"></script>
<script type="text/javascript" src="vendors/switchery/js/switchery.min.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.resize.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.stack.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.time.js"></script>
<script type="text/javascript" src="vendors/flotspline/js/jquery.flot.spline.min.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.categories.js"></script>
<script type="text/javascript" src="vendors/flotchart/js/jquery.flot.pie.js"></script>
<script type="text/javascript" src="vendors/flot.tooltip/js/jquery.flot.tooltip.min.js"></script>
<script type="text/javascript" src="vendors/jquery_newsTicker/js/newsTicker.js"></script>
<script type="text/javascript" src="vendors/countUp.js/js/countUp.min.js"></script>
<!--end of plugin scripts-->
<script type="text/javascript" src="js/pages/new_dashboard.js"></script>
@stop
