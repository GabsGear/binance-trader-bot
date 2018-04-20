<!DOCTYPE html>
<html>
<head>
    <title>ProtraderBot | Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="shortcut icon" href="../img/icon.png"/>
    <!--Global styles -->
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/css/components.css" />
    <link type="text/css" rel="stylesheet" href="../css/custom.css" />
    <!--End of Global styles -->
    <!--Plugin styles-->
    <link type="text/css" rel="stylesheet" href="../vendors/bootstrapvalidator/css/bootstrapValidator.min.css"/>
    <!--End of Plugin styles-->
    <link type="text/css" rel="stylesheet" href="../css/pages/login3.css"/>
</head>
<body class="login_backimg">
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
<div class="container">
    <div class="row">
        <div class="col-xl-6 push-xl-3 col-lg-8 push-lg-2 col-md-10 push-md-1 col-sm-10 push-sm-1 login_section">
            <div class="row">
                <div class="col-lg-8 push-lg-2 col-md-10 push-md-1 col-sm-12 login2_border login_section_top">
                    <div class="login_logo login_border_radius1">
                        <h3 class="text-center">
                            <img src="../img/logo.png" style="width:220px; height:25px;" /> 
                            <br />
                        </h3>
                    </div>
                    <div class="m-t-15">
                        <form method="POST" action="{{ route('customlogin') }}" id="login_validator">
                            {{ csrf_field() }}
                            <div class="form-group">
                                <div class="input-group">
                                    <input type="text" class="form-control b_r_20" name="email" value="{{ old('email') }}" placeholder="Email">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <input id="password" type="password" class="form-control b_r_20" name="password" placeholder="Password" required>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-12">
                                    <div class="text-center">
                                        <a href="{{route('register')}}">Ainda não é cadastrado?</a> | 
                                        <a href="{{route('email.password.get')}}">Perdeu sua senha?</a>
                                        <button type="submit" class="btn btn-success btn-block b_r_20 m-t-20">ENTRAR</button>
                                    </div>
                                </div>
                            </div>
                        </form>
                        @if(!empty($success))
                            <div class="alert alert-success">
                                {{ $success }}
                            </div>
                        @endif
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- global js -->
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/tether.min.js"></script>
<script type="text/javascript" src="../js/bootstrap.min.js"></script>
<!-- end of global js-->
<!--Plugin js-->
<script type="text/javascript" src="../vendors/bootstrapvalidator/js/bootstrapValidator.min.js"></script>
<script type="text/javascript" src="../vendors/jquery.backstretch/js/jquery.backstretch.js"></script>
<!--End of plugin js-->
<script type="text/javascript" src="../js/pages/login3.js"></script>
</body>

</html>