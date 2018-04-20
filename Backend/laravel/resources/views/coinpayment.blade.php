@inject('PaymentController', 'App\Http\Controllers\PaymentController')

<?php
	$req = array(
		'amount' => 50.00,
		'currency1' => 'USD',
		'currency2' => 'BTC',
		'merchant' => 'f52b660a92f4299714be645564075956'
		'item_name' => 'Protrader',
		'ipn_url' => '{{route(listen)}}'
	);
	// See https://www.coinpayments.net/apidoc-create-transaction for all of the available fields
?>

{{ $PaymentController->api_call($req) }}
