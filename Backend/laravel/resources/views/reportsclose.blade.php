@inject('TransController', 'App\Http\Controllers\TransactionController')
@inject('BotController', 'App\Http\Controllers\BotController')

@extends('layouts/default')
@section('content')
<header class="head">
    <div class="main-bar">
       <div class="row no-gutters">
           <div class="col-6">
               <h4 class="m-t-5">
                   <i class="fa fa-book"></i>
                   Ordens Finalizadas
               </h4>
           </div>
           <div class="col-6">
                <div class="row">
                    <div class="col-4"></div>
                    <div class="col-4"> 
                        DATA
                        {{ Form::open(['method' => 'POST', 'route' => ['trans.filter.date']]) }}        
                            <select name="date" class="form-control" onchange='this.form.submit()'>
                            <option selected disabled>Selecione...</option>
                                <?php $prev_time = mktime (0, 0, 0, date("m")  , date("d"), date("y")); 
                                for($i = 1; $i <= 30; $i++){
                                    $date = date('d/m/y', $prev_time);
                                    $prev_time = mktime (0, 0, 0, date("m")  , date("d")-$i, date("y")); ?>
                                    <option value="{{$date}}">{{$date}}</option>
                                <?php } ?>
                            </select>
                        {{ Form::close() }}
                    </div>
                    <div class="col-4">
                        BOT
                        {{ Form::open(['method' => 'POST', 'route' => ['trans.filter.name']]) }}        
                            <select name="name" class="form-control" onchange='this.form.submit()'>
                            <option selected disabled>Selecione...</option>
                                @foreach($BotController->getAllBots() as $bot)
                                <option value="{{$bot->name}}">{{$bot->currency}} | {{$bot->name}}</option>
                                @endforeach
                            </select>
                        {{ Form::close() }}
                    </div>
                </div>
           </div>
       </div>
    </div>
</header>
<div class="outer">
    <div class="inner bg-container">
        <div class="row">
            <div class="col-12">
                <div class="row">
                    <div class="col-sm-12 col-12">
                        <div class="table-responsive m-t-35">
                            <table class="table">
                                <thead>
                                <tr>
                                    <th><font size="2px">PAR</font></th>
                                    <th><font size="2px">VALOR COMPRA</font></th>
                                    <th><font size="2px">VALOR VENDA</font></th>
                                    <th><font size="2px">QUANTIA</font></th>
                                    <th><font size="2px">VAR.</font></th>
                                    <th><font size="2px">VAR.</font></th>
                                    <th><font size="2px">VAR.</font></th>
                                    <th><font size="2px">TAXA</font></th>
                                    <th><font size="2px">DATA-ABERTURA</font></th>
                                    <th><font size="2px">DATA-FECHAMENTO</font></th>
                                </tr>
                                </thead>
                                <?php  $total = 0; ?>
                                <tbody>
                                    @foreach($trans as $t)
                                    <?php 
                                        $fee = $TransController->getFee($t); 
                                        $lucro_bruto = ($t->sell_value-$t->buy_value)*$t->quantity;
                                        $lucro_liquido = $lucro_bruto-$fee;
                                        $lucro_usd = $lucro_liquido*8100*3.3;
                                        $percentage = $TransController->getPercentage($t);
                                        $market = explode('-',$t->currency)
                                    ?>
                                    <tr>
                                        <td>{{ $t->currency }}</td>
                                        <td>{{ number_format($t->buy_value, 8, '.', ' ') }}</td>
                                        <td>{{ number_format($t->sell_value, 8, '.', ' ') }}</td>
                                        <td>{{ $t->quantity}}</td>
                                        <td>{{ number_format($lucro_liquido, 8, '.', ' ') }} BTC</td>
                                        <td>{{ number_format($percentage, 2, '.', ' ') }}%</td>
                                        <td>{{ number_format($lucro_usd, 2, '.', ' ') }}USD</td>
                                        <td>{{ number_format($fee, 8, '.', ' ') }}</td>
                                        <td>{{ $t->date_open }}</td> 
                                        <td>{{ $t->date_close }}</td>
                                    </tr>
                                    @endforeach
                                </tbody>
                            </table>
                        </div>
                    </div> <!--DIUV 12 -->
                </div>
            </div>
        </div>
    </div>
</div>
<!-- /#content -->
<!-- Modal -->
</div>
</div>


<!-- /#content -->
<div id="right">
<div class="right_content">
<div class="well-small dark m-t-15">
    <div class="row m-0">
        <div class="col-lg-12 p-d-0">
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('blue_black_skin.css','css')">
                <div class="skin_blue skin_size b_t_r"></div>
                <div class="skin_blue_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('green_black_skin.css','css')">
                <div class="skin_green skin_size b_t_r"></div>
                <div class="skin_green_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('purple_black_skin.css','css')">
                <div class="skin_purple skin_size b_t_r"></div>
                <div class="skin_purple_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('orange_black_skin.css','css')">
                <div class="skin_orange skin_size b_t_r"></div>
                <div class="skin_orange_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('red_black_skin.css','css')">
                <div class="skin_red skin_size b_t_r"></div>
                <div class="skin_red_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <div class="skinmulti_btn" onclick="javascript:loadjscssfile('mint_black_skin.css','css')">
                <div class="skin_mint skin_size b_t_r"></div>
                <div class="skin_mint_border skin_shaddow skin_size b_b_r"></div>
            </div>
            <!--</div>-->
            <div class="skin_btn skinsingle_btn skin_blue b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('blue_skin.css','css')"></div>
            <div class="skin_btn skinsingle_btn skin_green b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('green_skin.css','css')"></div>
            <div class="skin_btn skinsingle_btn skin_purple b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('purple_skin.css','css')"></div>
            <div class="skin_btn  skinsingle_btn skin_orange b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('orange_skin.css','css')"></div>
            <div class="skin_btn skinsingle_btn skin_red b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('red_skin.css','css')"></div>
            <div class="skin_btn skinsingle_btn skin_mint b_r height_40 skin_shaddow"
                 onclick="javascript:loadjscssfile('mint_skin.css','css')"></div>
        </div>
        <div class="col-lg-12 text-center m-t-15">
            <button class="btn btn-dark button-rounded"
                    onclick="javascript:loadjscssfile('black_skin.css','css')">Dark
            </button>
            <button class="btn btn-secondary button-rounded default_skin"
                    onclick="javascript:loadjscssfile('default_skin.css','css')">Default
            </button>
        </div>
    </div>
</div>
</div>
</div>
@stop
<!-- /#wrap -->
