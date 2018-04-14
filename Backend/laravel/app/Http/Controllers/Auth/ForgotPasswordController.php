<?php

namespace App\Http\Controllers\Auth;


use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\SendsPasswordResetEmails;
use Illuminate\Http\Request;
use DB;
use Hash;
use Redirect;

class ForgotPasswordController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Password Reset Controller
    |--------------------------------------------------------------------------
    |
    | This controller is responsible for handling password reset emails and
    | includes a trait which assists in sending these notifications from
    | your application to your users. Feel free to explore this trait.
    |
    */

    use SendsPasswordResetEmails;
    

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest');
    }

    public function getReset($token) {
        return view('auth.forgotpassreset', compact('token'));
    }

    public function postReset(Request $request) {   
        $check = ForgotPasswordController::checkToken($request['email'], $request['token']);
        if($request['password'] == $request['password_confirmation'] and $check == 1) {           
            $user = DB::table('users')->where('email', $request['email'])->get();
            $pass = Hash::make($request->input('password'));              
            DB::table('users')->where('id', $user[0]->id)->update(['password' => $pass]);
            return view('login')->withSuccess('Senha resetada com sucesso, efetue o login!');
        }
        return Redirect::back()->withErrors(['Dados incorretos.']);
    }

    public function checkToken($email, $token) {
        return DB::table('password_resets')->where('email', $email)->where('token', $token)->get()->count();
    }

}
