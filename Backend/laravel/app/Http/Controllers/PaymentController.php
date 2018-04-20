<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use RonMelkhior\CoinpaymentsIPN\IPN;
use Charts;
use App\Transaction;
use App\Bot;
use DB;
use Auth;
use App\Http\Controllers\ProcessController;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class PaymentController extends Controller {


    public function callbackError(int $errorCode, string $errorMessage) {
	    throw new Exception('#'.$errorCode.' There was a problem establishing integrity with the request: '.$errorMessage);
    }


    public function api_call($req = array()) {        
		// Set the API command and required fields
        $req['version'] = 1;
		$req['cmd'] = 'create_transaction';
		$req['key'] = '53fd5ff818629a2c87b9e87ca789070f56941f68c6adbb56e59523151694c9d8';
		$req['format'] = 'json'; //supported values are json and xml

		// Generate the query string
		$post_data = http_build_query($req, '', '&');
	    
		// Calculate the HMAC signature on the POST data
		$hmac = hash_hmac('sha512', $post_data, 'f34658917221c903872A2936425Afe04f0111f50685f59b58BD23410b082291D');
	    
		// Create cURL handle and initialize (if needed)
		$ch = curl_init('https://www.coinpayments.net/api.php');
		curl_setopt($ch, CURLOPT_FAILONERROR, TRUE);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
		curl_setopt($ch, CURLOPT_HTTPHEADER, array('HMAC: '.$hmac));
		curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
	    
		return curl_exec($ch);                
	}

	public function listen() {
		$merchant_id = 'f52b660a92f4299714be645564075956';
		$secret = 'libano25258';

		if (!isset($_SERVER['HTTP_HMAC']) || empty($_SERVER['HTTP_HMAC'])) {
			die("No HMAC signature sent");
		}
		  
		$merchant = isset($_POST['merchant']) ? $_POST['merchant']:'';
		if (empty($merchant)) {
		die("No Merchant ID passed");
		}
		  
		if ($merchant != $merchant_id) {
			die("Invalid Merchant ID");
		}
		
		$request = file_get_contents('php://input');
		if ($request === FALSE || empty($request)) {
			die("Error reading POST data");
		}
		
		$hmac = hash_hmac("sha512", $request, $secret);
		if ($hmac != $_SERVER['HTTP_HMAC']) {
			die("HMAC signature does not match");
		}

	}



}
