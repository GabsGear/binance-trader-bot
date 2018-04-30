@inject('UserController', 'App\Http\Controllers\UserController')

<!doctype html>
<html class="no-js" lang="en">

<head>
    <meta charset="UTF-8">
    <title>ProTraderBot</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="http://painel.protraderbot.com/img/icon.png"/>

    <!--global styles-->
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/css/components.css"/>
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/css/custom.css"/>
    <!-- end of global styles-->
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/vendors/c3/css/c3.min.css"/>
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/vendors/switchery/css/switchery.min.css"/>
    <link type="text/css" rel="stylesheet" href="http://painel.protraderbot.com/css/pages/new_dashboard.css"/>
</head>

<body class="body">

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
        <img src="../img/loader.gif" style=" width: 40px;" alt="loading...">
    </div>
</div>

<div id="wrap">
    <div id="top">
        <!-- .navbar -->
        <nav class="navbar navbar-static-top">
            <div class="container-fluid m-0"> 
                <a class="navbar-brand float-left" href="{{route('dashboard')}}">
                    <img class="admin_img" style="width:180px;" src="http://painel.protraderbot.com/img/logo.png" /> 
                </a>
                <div class="menu">
                    <span class="toggle-left" id="menu-toggle">
                        <i class="fa fa-bars"></i>
                    </span>
                </div>
                <div class="topnav dropdown-menu-right float-right">
                    <div class="btn-group">
                        <div class="user-settings no-bg">
                            <button type="button" class="btn btn-default no-bg micheal_btn" data-toggle="dropdown" aria-expanded="true">
                                <img src="/img/avatar.jpg" class="admin_img2 img-thumbnail rounded-circle avatar-img" alt="avatar" >
                                <strong>{{$UserController->getUser()->email}}</strong>
                            </button>
                        </div>

                    </div>
                </div>
            </div>
            <!-- /.container-fluid -->
        </nav>
        <!-- /.navbar -->
        <!-- /.head -->
    </div>
    <!-- /#top -->
    <div class="wrapper">
        <div id="left">
            <div class="menu_scroll">
                <ul id="menu">
                    <li>
                        <a href="{{route('dashboard')}}">
                            <i class="fa fa-home"></i>
                            <span class="link-title menu_hide">&nbsp;Inicio</span>
                        </a>
                    </li>
                    <li class="dropdown">
                        <a href="javascript:;">
                            <i class="fa fa-wpforms"></i>
                            <span class="link-title menu_hide">&nbsp; Relatorios</span>
                            <span class="fa arrow menu_hide"></span>
                        </a>
                        <ul class="collapse" aria-expanded="false" style="">
                            <li>
                            <a href="{{route('reports.open')}}">
                                <i class="fa fa-book"></i>
                                <span class="link-title menu_hide">&nbsp;Ordens Abertas
                                </span>
                            </a>
                            </li>
                            <li>
                            <a href="{{route('reports.close')}}">
                                <i class="fa fa-book"></i>
                                <span class="link-title menu_hide">&nbsp;Ordens Finalizadas
                                </span>
                            </a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="{{route('account')}}">
                            <i class="fa fa-cogs"></i>
                            <span class="link-title menu_hide">&nbsp;Conta
                            </span>
                        </a>
                    </li>
                    <li>
                        <a href="http://protraderbot.com/blog/contato/" target="_blank">
                            <i class="fa fa-envelope-o"></i>
                            <span class="link-title menu_hide">&nbsp;Suporte
                            </span>
                        </a>
                    </li>
                    <li>
                        <a href="{{ route('acc.logout') }}" onclick="event.preventDefault();document.getElementById('logout-form').submit();">
                            <i class="fa fa-sign-out"></i>
                            <span class="link-title menu_hide">&nbsp;Sair
                            </span>
                        </a>

                        <form id="logout-form" action="{{ route('acc.logout') }}" method="POST" style="display: none;">
                            {{ csrf_field() }}
                        </form>
                    </li>
                </ul>
                <!-- /#menu -->
            </div>
        </div>    
        <!-- /#content -->
        <div id="content" class="bg-container">
            @yield('content')
        </div>
</div>
<!-- /#wrap -->
<!-- global scripts-->
<script type="text/javascript" src="http://painel.protraderbot.com/js/components.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/js/custom.js"></script>
<!-- global scripts end-->
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/slimscroll/js/jquery.slimscroll.min.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/raphael/js/raphael-min.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/d3/js/d3.min.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/c3/js/c3.min.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/switchery/js/switchery.min.js"></script>

<script type="text/javascript" src="http://painel.protraderbot.com/vendors/jquery_newsTicker/js/newsTicker.js"></script>
<script type="text/javascript" src="http://painel.protraderbot.com/vendors/countUp.js/js/countUp.min.js"></script>
<!--end of plugin scripts-->

</body>
</html>
