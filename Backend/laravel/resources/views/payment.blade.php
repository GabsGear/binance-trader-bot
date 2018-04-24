@inject('UserController', 'App\Http\Controllers\UserController')
@inject('PaymentController', 'App\Http\Controllers\PaymentController')

@extends('layouts/default')
@section('content')
<header class="head">
    <div class="main-bar">
       <div class="row no-gutters">
           <div class="col-6">
               <h4 class="m-t-5">
                   <i class="fa fa-bitcoin"></i>
                   Pagamento
               </h4>
           </div>
       </div>
    </div>
</header>
<div class="outer">
    <div class="inner bg-container">
        <div class="row">
            <div class="col-sm-6 col-6">
                <div class="card">
                    <div class="card-header bg-white">
                        Gerar Fatura
                    </div>
                    <div class="col-lg-12" style="padding:10px;">
                        @if($errors->any())
                            <div class="alert alert-danger">
                                {{$errors->first()}}
                            </div>
                        @endif
                        @if(!empty($success))
                            <div class="alert alert-success">
                                {{ $success }}
                            </div>
                        @endif
                    </div>
                    <div class="col-lg-8 input_field_sections">
                        <form class="form-horizontal" method="POST" action="{{ route('payment.create') }}">
							{{ csrf_field() }}
							<label>Plano</label></br>
							<select name="item_name" class="form-control">
								<option selected disabled>Selecione...</option>
								<option value="ProTraderBot-Prata-30-dias">Prata 30 dias - 5 bots - 20%OFF</option>
                                <option value="ProTraderBot-Prata-90-dias">Prata 90 dias - 5 bots - 40%OFF</option>
                                <option value="ProTraderBot-Ouro-30-dias">Ouro 30 dias - 10 bots - 20%OFF</option>
								<option value="ProTraderBot-Ouro-90-dias">Ouro 90 dias - 10 bots - 40%OFF</option>
							</select></br>
							<label>Moeda</label></br>
							<select name="currency2" class="form-control">
								<option selected disabled>Selecione...</option>
								<option value="BTC">Bitcoin</option>
								<option value="LTC">Litecoin</option>
								<option value="ETH">Etherum</option>
							</select></br>
							<button type="submit" class="btn btn-success">Criar Fatura</button>
							</br></br>
                    	</form>
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
