<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use Charts;
use App\Bot;
use App\Transaction;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class ChartController extends Controller
{
    public function home(){
        return view('chart');
    }
    public static function getChart($id) {
        $bot =  Bot::find($id);
        
        $data = ChartController::getData($bot->id);
        #ChartController::decision($data);

        $chart = Charts::multi('line', 'highcharts')
    			->title($bot->currency)
    			->dataset('Close', $data['close'])
                ->labels($data['timestamp'])
    			->dimensions(0, 400);

        return array($chart, $data); 
    }

    public static function getData($id) {
        $path = "/var/www/html/logs/".$id.".json";
        $file = file_get_contents($path);
    	$data = json_decode($file, true); // decode the JSON into an associative array
        return $data;
    }

}