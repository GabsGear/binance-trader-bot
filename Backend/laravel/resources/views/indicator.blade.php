@inject('TransController', 'App\Http\Controllers\TransactionController')

@extends('layouts/default')
@section('content')
<script type="text/javascript" src="http://198.50.194.124/js/moment.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    let full_url = document.URL;
    let url_array = full_url.split('/');
    let bot_id = url_array[url_array.length-1];

    function toggleDataSeries(e) {
        if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        } else {
            e.dataSeries.visible = true;
        }
        e.chart.render();
    }

    setInterval(function() {  
        let json_candles = [];
        let chart  = [];
        let candlePoints = [];
        let buyLine = [];
        let sellLine = [];
        let stoplossLine = [];
        let indicator_url = "http://198.50.194.124/bot/candles/"+bot_id;
        let trans_url = "http://198.50.194.124/bot/trans/"+bot_id;
        $.getJSON(indicator_url, function(json_candles) {
            return json_candles;
        }).then(function(json_candles) {
            $.getJSON(trans_url, function(trans) {
                let size = json_candles.result.length;
                let candles = json_candles.result.slice(size-40, size).map(function (candle) {
                    return [candle.T, candle.O, candle.H, candle.L, candle.C]
                });
                let price_buy  = 0;
                let price_sell = 0;
                let dataChart   = [];
                let stripLines = [];
                if(trans.length > 0) {
                    let t = trans[0];
                    if(t.selled == 0) {
                        stripLines = [
                            {value: t.buy_value, label: "BUY -> "+t.buy_value, color:"black",labelFontColor: "black", legend:"BUY SIGNAL"}, 
                        ];
                        dataChart = [{ //DATACHART SELLED = 0
                                type: "candlestick",
                                name:"Prices",
                                dataPoints: candlePoints
                            },
                        ];  // FIM DATACHART
                    } else {
                        stripLines = [
                            {value: t.buy_value, color:"#00cc99", label: "BUY -> "+t.buy_value, labelFontColor:"#00cc99", legend: "BUY SIGNAL"}, 
                            {value: t.sell_value, color:"#EF6F6C", label: "SELL -> "+t.sell_value,  labelFontColor:"#EF6F6C",  legend: "SELL SIGNAL"}, 
                        ];
                        dataChart = [{ //DATACHART SELLED = 1
                                type: "candlestick",
                                name: "Prices",
                                color: "#525252",
                                dataPoints: candlePoints,
                                risingColor: "#00cc99",
		                        fallingColor: "#EF6F6C",
                            },
                        ]; // FIM DATACHART
                    };
                } else {
                    dataChart = [{ //DATACHART NORMAL
                            type: "candlestick",
                            name: "Prices",
                            dataPoints: candlePoints
                        }
                    ]; // FIM DATACHART
                };
                
                //PLOTANDO GRAFICO CANVASJS
                chart = new CanvasJS.Chart("chartContainer", {
                    animationEnabled: true,
                    theme: "light1", // "light1", "light2", "dark1", "dark2"
                    axisX: {
                        interval:0,
                        valueFormatString: 'HH:mm',
                        crosshair: {
                            enabled: true,
                            snapToDataPoint: true,
                        },
                    },
                    axisY: {
                        valueFormatString: "0.00000000",
                        includeZero: false,
                        title: "Price",
                        showOnTop: true,
                        gridThickness: 1,
                        gridColor: "#CCCCCC",
                        stripLines: stripLines,
                        crosshair: {
                            enabled: true,
                            snapToDataPoint: true,
                            labelFormatter: function(e) {
                                return CanvasJS.formatNumber(e.value, "0.00000000");
                            }
                        }
                    },
                    axisY2: {
                        title: "",
                        tickLength: 0,
                        lineThickness: 0,
                        margin: 0,
                    },
                    legend: {
                        reversed: true,
                        cursor: "pointer",
                        itemclick: toggleDataSeries
                    }, 
                    data: dataChart,
                }); //FIM CONFIG CANVAJS OBJECT
                
                candles.forEach(function(candle, index) {
                    var utc  = moment.utc(candle[0]);
                    candlePoints.push({
                        x: utc.toDate(),
                        y: [
                            parseFloat(candle[1]),
                            parseFloat(candle[2]),
                            parseFloat(candle[3]),
                            parseFloat(candle[4])
                        ]
                    });
                    chart.render();
                });

                if(trans.length > 0) {
                    let t = trans[0];
                    if(t.selled == 0) {
                        let html = "Valor: "+t.buy_value+"</br> Data-Hora: "+t.date_open;
                        $("#buy_signal").html(html);
                        $("#sell_signal").html("nenhum sinal...");
                    } else {
                        let html1 = "Valor: "+t.buy_value+"</br>Data-Hora: "+t.date_open;
                        let html2 = "Valor: "+t.sell_value+"</br> Data-Hora: "+t.date_close;
                        $("#buy_signal").html(html1);
                        $("#sell_signal").html(html2);
                    }
                }
        });
        });
    }, 10000);
</script>
<header class="head">
    <div class="main-bar">
       <div class="row no-gutters">
           <div class="col-12">
               <h4 class="m-t-5">
                   <i class="fa fa-line-chart"></i>
                   Indicador em Tempo Real
               </h4>
           </div>
       </div>
    </div>
</header>
<div class="outer">
    <div class="inner bg-container">
        <div class="row">
            <div class="col-sm-4 col-4">
                <div class="card">
                    <div class="card-header bg-white">Sinais</div>
                        <div class="card-body">
                            <ul>
                                <li>
                                <strong>Estratégia:</strong>@if($bot->strategy_buy == 0)
                                    Contra Turtle
                                @elseif($bot->strategy_buy == 1)
                                    Inside Bar
                                @elseif($bot->strategy_buy == 2)
                                    Double UP
                                @else
                                    Pivot UP
                                @endif
                                </li>
                                <li><strong>Tempo gráfico:</strong> {{$bot->period}}</li>
                                <li><strong>Corretora:</strong> Bittrex</li>
                                <li><strong>Par:</strong> {{$bot->currency}}</li>
                            </ul>
                            <div class="alert alert-success alert-dismissable">
                                <strong>Sinal de Compra</strong>
                                <p><div id="buy_signal"></div></p>
                            </div>

                            <div class="alert alert-danger alert-dismissable">
                                <strong>Sinal de Venda</strong>
                                <p><div id="sell_signal"></div></p>
                            </div>
                        </div>
                </div>
            </div>
            <div class="col-sm-8 col-8">
                <div class="card">
                    <div class="card-header bg-white">Gráfico Real Time</div>
                        <div id="chartContainer" style="height: 400px; width: 100%;"></div>
                        <script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
                    </div>
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
