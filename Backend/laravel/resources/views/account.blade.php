@inject('UserController', 'App\Http\Controllers\UserController')

@extends('layouts/default')

@section('content')
<header class="head">
    <div class="main-bar">
       <div class="row no-gutters">
           <div class="col-6">
               <h4 class="m-t-5">
                   <i class="fa fa-cogs"></i>
                   Configurações da Conta
               </h4>
           </div>
       </div>
    </div>
</header>
<div class="outer">
    <div class="inner bg-container">
        <div class="row">
            <div class="col-sm-4 col-12">
                <div class="card">
                    <div class="card-header bg-white">
                        Alterar Senha
                    </div>
                    <div class="col-lg-12 input_field_sections">
                        <form class="form-horizontal" method="POST" action="{{ route('acc.changepass') }}">
                        {{ csrf_field() }}
                        <label>Senha Atual</label>
                        <input id="password" type="password" class="form-control" name="oldpass" required>
                        <label>Nova Senha</label>
                        <input id="password" type="password" class="form-control" name="password" required>
                        <label>Confirmar Nova Senha</label>
                        <input id="password-confirm" type="password" class="form-control" name="password_confirmation" required>
                        </br>
                        <button class="btn btn-success">Salvar</button>
                        </br></br>
                    </form>
                    </div>
                </div>
            </div>
            <div class="col-sm-4 col-12">
                <div class="card">
                    <div class="card-header bg-white">
                        Chaves da API Bittrex - Estado: 
                        @if($UserController->check_bittrex() == true)
                            <font color="green"><b>ONLINE</b></font>
                        @else
                            <font color="red"><b>OFFLINE</b></font>
                        @endif
                    </div>
                    <div class="col-lg-12 input_field_sections">
                        @if($UserController->getUser()->premium > 0)
                        <form method="POST" action="{{route('acc.api.bittrex')}}">
                            {{ csrf_field() }}
                            <label>Key</label>
                            <?php 
                                if(strlen($UserController->getUser()->bit_api_key) > 2) {?>
                                    <input type="text" class="form-control" name="bit_api_key" value="******************">
                                <?php }
                                else { ?>
                                    <input type="text" class="form-control" name="bit_api_key" value="">
                                <?php }
                            ?>
                            <label>Secret</label>
                            <?php 
                                if(strlen($UserController->getUser()->bit_api_secret) > 2) {?>
                                    <input type="text" class="form-control" name="bit_api_secret" value="******************">
                                <?php }
                                else { ?>
                                    <input type="text" class="form-control" name="bit_api_secret" value="">
                                <?php }
                            ?>
                            </br>
                            <div style="float:right">
                                <a href="http://protraderbot.com/blog/como-faco-para-encontrar-minha-chave-de-api-na-bittrex-com/" target="_blank">Instruções</a> 
                            </div>
                            <div style="float:left">
                                <button class="btn btn-success">Salvar</button>
                            </div>
                            </br></br>
                        </form>
                        @endif
                    </div>
                </div>
            </div>

            <div class="col-sm-4 col-12">
                <div class="card">
                    <div class="card-header bg-white">
                        Chaves API Binance - Estado: 
                        @if($UserController->check_binance() == 1)
                            <font color="green"><b>ONLINE</b></font>
                        @else
                            <font color="red"><b>OFFLINE</b></font>
                        @endif
                    </div>
                    <div class="col-lg-12 input_field_sections">
                        @if($UserController->getUser()->premium > 0)
                        <form method="POST" action="{{route('acc.api.binance')}}">
                            {{ csrf_field() }}
                            <label>Key</label>
                            <?php 
                                if(strlen($UserController->getUser()->bin_api_key) > 2) {?>
                                    <input type="text" class="form-control" name="bin_api_key" value="******************">
                                <?php }
                                else { ?>
                                    <input type="text" class="form-control" name="bin_api_key" value="">
                                <?php }
                            ?>
                            <label>Secret</label>
                            <?php 
                                if(strlen($UserController->getUser()->bin_api_secret) > 2) {?>
                                    <input type="text" class="form-control" name="bin_api_secret" value="******************">
                                <?php }
                                else { ?>
                                    <input type="text" class="form-control" name="bin_api_secret" value="">
                                <?php }
                            ?>
                            </br>
                            <div style="float:right">
                                <a href="http://protraderbot.com/blog/como-faco-para-encontrar-minha-chave-de-api-na-bittrex-com/" target="_blank">Instruções</a> 
                            </div>
                            <div style="float:left">
                                <button class="btn btn-success">Salvar</button>
                            </div>
                            </br></br>
                        </form>
                        @endif
                    </div>
                </div>
            </div>

        </div>
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
<!-- /#wrap -->
@stop
