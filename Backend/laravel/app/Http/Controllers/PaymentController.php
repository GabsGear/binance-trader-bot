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


    public function check() {
        $ipn = new IPN();
        $ipn->setMerchantID('f52b660a92f4299714be645564075956')->setIPNSecret('libano252528');
        try {
            if ($ipn->validate($_POST, $_SERVER)) {
                return "pagamento efetuado com sucesso.";
            } else {
                return "pagamento pendente";
            }
        } catch (RonMelkhior\CoinpaymentsIPN\Exceptions\InvalidRequestException $e) {
            return "erro The IPN data was not valid to begin with (missing data, invalid IPN method).";
        } catch (RonMelkhior\CoinpaymentsIPN\Exceptions\InsufficientDataException $e) {
            return "Sufficient data provided, but either the merchant ID or the IPN secret didn't match.";
        } catch (RonMelkhior\CoinpaymentsIPN\Exceptions\FailedPaymentException $e) {
            return "IPN worked, but the payment has failed (PayPal refund/cancelled/timed out).";
        }
    }




}
