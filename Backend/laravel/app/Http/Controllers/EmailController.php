<?php

namespace App\Http\Controllers;

use Mail;
use Illuminate\Http\Request;
use DB;
use App\PassReset;
use Redirect;

class EmailController extends Controller
{
    public function getEmailForgotPass() {
        return view('forgotpass');
    }

    public function postEmailForgotPass(Request $request) {
        $email = trim($request['email']);
        $email = stripslashes($email);
        $email = htmlspecialchars($email);

        $verify_user = DB::table('users')->where('email', $email)->get()->count();
        if($verify_user > 0) {
            $token = str_random(20);
            DB::table('password_resets')->insert(
                ['email' => $email, 'token' => $token, 'created_at' => date('Y-m-d H:i:s')]
            );
            $data = array(
                'token'=> $token,
            );
            Mail::send('emails.password', $data, function ($message) use($email) {
                $message->from('no-reply@protraderbot.com','Protraderbot');
                $message->to($email);
                $message->subject('Link Para Reset de Senha');
            });
            return view('forgotpass')->withSuccess('Link enviado com sucesso, pode demorar ate 5 minutos, verifique sua caixa de spam!');
        };
        return Redirect::back()->withErrors(['Email nao existe.']);
    }
}
