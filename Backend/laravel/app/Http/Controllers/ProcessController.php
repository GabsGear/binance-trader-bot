<?php
namespace App\Http\Controllers;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use App\Bot;

class ProcessController extends Controller
{
    public static function getProcessId($bot_id) {
	    return Bot::find($bot_id)->pid;
	}

	public static function checkBOT($bot_id) {
		$status = shell_exec('ps -hp' . ProcessController::getProcessId($bot_id));
	    // se positivo (ligado), retorna true, caso contrário, retorna false;
	    return $status;
	}
	
	public function startBOT($bot_id) {
		chdir('/home');
		if(ProcessController::checkBOT($bot_id) == NULL){
        	shell_exec('sudo chown -R www-data.www-data /home > /dev/null &');
    		shell_exec('sudo python main.py '.$bot_id.' > /dev/null &');
    	}
    	echo 'fui';
    	return redirect()->route('dashboard');

	}
	
	public function stopBOT($bot_id) {
		$pid = Bot::find($bot_id)->pid;
		if(ProcessController::checkBOT($bot_id) != NULL) {
    		shell_exec('sudo kill -9 '.$pid.' > /dev/null &');
    	}
    	return redirect()->route('dashboard');
	}
}

?>