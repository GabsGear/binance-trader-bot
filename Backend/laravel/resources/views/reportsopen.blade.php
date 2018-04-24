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
                   Ordens Abertas
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
                    <div class="col-sm-12 col-12">
                        <div class="table-responsive m-t-35">
                            <table class="table table-bordered table-striped flip-content">
                                <thead class="flip-content">
                                <tr>
                                    <th><font size="2px">PAR</font></th>
                                    <th><font size="2px">VALOR COMPRA</font></th>
                                    <th><font size="2px">QUANTIA</font></th>
                                    <th><font size="2px">DATA-ABERTURA</font></th>
                                    <th></th>
                                </tr>
                                </thead>
                                <tbody>
                                @foreach($TransController->getAll(0) as $trans)
                                <tr>
                                    <td>{{$trans->currency}}</td>
                                    <td>{{ number_format($trans->buy_value, 8, '.', ' ') }}</td>
                                    <td>{{$trans->quantity}}</td>
                                    <td>{{$trans->date_open}}</td>
                                    <td>
                                        {{ Form::open(['method' => 'DELETE', 'route' => ['trans.delete', $trans->id]]) }}
                                            <button type="submit" class="btn btn-danger"><i class="fa fa-trash"></i></button>
                                        {{ Form::close() }}
                                    </td>
                                @endforeach
                                </tr>
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
