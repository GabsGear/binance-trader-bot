<?php

namespace App\Http\Controllers;

use Mail;
use Illuminate\Http\Request;

class EmailController extends Controller
{
    public function send()
    {
        $data = array(
            'name' => "Learning Laravel",
        );
        Mail::send('emails.send', $data, function ($message) {
			$message->from('contato@protraderbot.com','Protraderbot');
			$message->to('alechaito@gmail.com');
			$message->subject('Contact form submitted on domainname.com ');
 		});
    }
}
