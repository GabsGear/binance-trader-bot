<!DOCTYPE html>
<html>
<head>
    <title>ProtraderBot| Cadastro</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="shortcut icon" href="../img/icon.png"/>
    <!--Global styles -->
    <link type="text/css" rel="stylesheet" href="css/components.css" />
    <link type="text/css" rel="stylesheet" href="css/custom.css" />
    <!--End of Global styles -->
    <!--Plugin styles-->
    <link type="text/css" rel="stylesheet" href="vendors/bootstrapvalidator/css/bootstrapValidator.min.css"/>
    <link type="text/css" rel="stylesheet" href="vendors/wow/css/animate.css"/>
    <!--End of Plugin styles-->
    <link type="text/css" rel="stylesheet" href="css/pages/login2.css"/>



</head>
<body class="login_background">
<div class="preloader" style=" position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 100000;
  backface-visibility: hidden;
  background: #ffffff;">
    <div class="preloader_img" style="width: 200px;
  height: 200px;
  position: absolute;
  left: 48%;
  top: 48%;
  background-position: center;
z-index: 999999">
        <img src="../img/loader.gif"  style=" width: 40px;" alt="loading...">
    </div>
</div>
<div class="container wow fadeInDown" data-wow-duration="1s" data-wow-delay="0.5s">
    <div class="row">
        <div class="col-xl-6 push-xl-3 col-lg-6 push-lg-3 col-md-8 push-md-2 col-sm-8 push-sm-2 col-10 push-1">
            <div class="row">
                <div class="col-lg-8 push-lg-2 col-md-10 push-md-1 col-sm-12 login_image login_section register_section_top">
                    <div class="login_logo login_border_radius1">
                        <h3 class="text-center text-white">
                            <img src="../img/logo.png" style="width:220px; height:25px;" /> 
                        </h3>
                    </div>
                    <div class="m-t-15">
                       <form class="form-horizontal" method="POST" action="{{ route('register') }}" onsubmit="return checkCheckBox(this)">
                        {{ csrf_field() }}

                        <div class="form-group{{ $errors->has('name') ? ' has-error' : '' }}">

                            <div class="col-md-12">
                                <input id="name" type="text" class="form-control" name="name" value="{{ old('name') }}" placeholder="Nome Completo" required autofocus>
                                @if ($errors->has('name'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('name') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('email') ? ' has-error' : '' }}">

                            <div class="col-md-12">
                                <input id="email" type="email" class="form-control" name="email" value="{{ old('email') }}" placeholder="Email" required>

                                @if ($errors->has('email'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('email') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password') ? ' has-error' : '' }}">
                            <div class="col-md-12">
                                <input id="password" type="password" class="form-control" name="password" placeholder="Senha" required>

                                @if ($errors->has('password'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group">

                            <div class="col-md-12">
                                <input id="password-confirm" type="password" class="form-control" name="password_confirmation" placeholder="Confirmar Senha" required>
                            </div>
                        </div>
                         
                        <div class="form-group">
                            <div class="col-md-12 col-md-offset-4">
                                
                                     <!-- jao fez -->

                                    
                                         <input type="checkbox" value="0" name="agree"> <a style="color:#525252;" >Aceito os <a href="http://198.50.194.124/termos" style="color:#fd4326; text-decoration: underline"> termos de uso </a></a>
                                         <button type="submit" class="btn btn-success btn-block b_r_20 m-t-20">REGISTRAR</button> 
                                     

                                    <!-- terminou -->
                                    <div class="text-center">
                                        <a href="{{route('login')}}">Já tem uma conta?</a>
                                     </div>
                                   
                              <!-- <button type="submit" class="btn btn-success btn-block b_r_20 m-t-20">REGISTRAR</button> -->
                            </div>
                        </div>
                    </form> 
                  
                    </div>
                    @if($errors->any())
                        <h4>{{$errors->first()}}</h4>
                    @endif
                </div>
            </div>
        </div>
    </div>
</div>
<!-- global js -->
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/tether.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<!-- end of global js-->
<!--Plugin js-->
<script type="text/javascript" src="vendors/bootstrapvalidator/js/bootstrapValidator.min.js"></script>
<script type="text/javascript" src="vendors/wow/js/wow.min.js"></script>
<!--End of plugin js-->
<script type="text/javascript" src="js/pages/login2.js"></script>

<!-- Js feito pela equipe Protradeboat -->
<script type="text/javascript" src="js/jsProtradebot.js"></script>

</body>

</html>