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
Use Redirect;

class PaymentController extends Controller {


    public function create(Request $post) {        
		// Set the API command and required fields
		$req = array();
		$req['item_name'] = $post['item_name'];
		$req['currency2'] = $post['currency2'];
		$req['merchant_id'] = 'f52b660a92f4299714be645564075956';
		$req['currency1'] = 'USD';
		$req['version'] = 1;
		$req['cmd'] = 'create_transaction';
		$req['key'] = '53fd5ff818629a2c87b9e87ca789070f56941f68c6adbb56e59523151694c9d8'; 
		$req['format'] = 'json'; //supported values are json and xml
		$req['buyer_email'] = Auth::User()->email;

		if($req['item_name'] == "ProTraderBot-Prata-30-dias"){
			$req['amount'] = 48.0;
		}
		else if($req['item_name'] == "ProTraderBot-Prata-90-dias"){
			$req['amount'] = 109.0;
		}
		else if($req['item_name'] == "ProTraderBot-Ouro-30-dias"){
			$req['amount'] = 72.0;
		}
		else if($req['item_name'] == "ProTraderBot-Ouro-90-dias"){
			$req['amount'] = 163.0;
		}
		else {
			die("Plano inexistente");
		}

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
		$json = json_decode(curl_exec($ch), true);
		if($json['error'] == 'ok') {
			$data = $json['result'];
			DB::table('payments')->insert(
				[
					'amount' => $data['amount'], 
					'currency' => $req['currency2'], 
					'item_name' => $req['item_name'], 
					'tx_id' => $data['txn_id'], 
					'address' => $data['address'],
					'user_id' => Auth::User()->id,
					'status' => 0
				]
			);
			EmailController::postPayment($data['status_url'], $data['txn_id'], $req['item_name'], $data['amount'], $req['currency2']);
			return view('payment')->withSuccess('A fatura foi gerada com sucesso e foi encaminhada para seu e-mail, verifique sua caixa de spam!');
		}
		return view('payment');
	}


	public function check_payments() {
		$payments = DB::table('payments')->where('status', 0)->get();
		foreach($payments as $pay) {
			echo "VERIFICANDO TRANS ID:".$pay->tx_id;
			$data = PaymentController::getInfo($pay->tx_id);
			if($json['error'] == 'ok') {
				if ($data['status'] == 100) {
					switch($pay->item_name) {
						case 'ProTraderBot-Prata-30-dias':
							$user->premium == 1;
							$user->expire_date == date('Y-m-d', strtotime("+30 days"));
							break;
						case 'ProTraderBot-Prata-90-dias':
							$user->premium == 1;
							$user->expire_date == date('Y-m-d', strtotime("+90 days"));
							break;	
						case 'ProTraderBot-Ouro-30-dias':
							$user->premium == 2;
							$user->expire_date == date('Y-m-d', strtotime("+30 days"));
							break;
						case 'ProTraderBot-Ouro-90-dias':
							$user->premium == 2;
							$user->expire_date == date('Y-m-d', strtotime("+90 days"));
							break;
					}
				}
				DB::table('payments')
				->where('id', $pay->id)
				->update(['status' => $data['status']]);	
			}
		}
	}
	


}
