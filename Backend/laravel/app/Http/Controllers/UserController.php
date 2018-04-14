<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use Auth;
use Hash;

class UserController extends Controller
{

    public function getUser() {
        return Auth::user();
    }

    public function updateAPI(Request $request) {
        $user = Auth::user();
        $user->api_secret = UserController::test_input($request['api_secret']);
        $user->api_key = UserController::test_input($request['api_key']);
        $user->save();
        return redirect()->route('account');
    }

    public function reset(Request $request) {
        $current_password = Auth::User()->password;           
        if(Hash::check($request->input('oldpass'), $current_password) AND $request->input('password') == $request->input('password_confirmation')) {           
            $user_id = Auth::User()->id;                       
            $obj_user = User::find($user_id);
            $obj_user->password = Hash::make($request->input('password'));
            $obj_user->save(); 
        }
        return redirect()->route('account');
    }

    public function logout(Request $request) {
        Auth::logout();
        $request->session()->flush();
        $request->session()->regenerate();
        return redirect()->route('login');
    }

    public static function bittrexbalance() {
        $nonce = time();
        $user  = Auth::User();
        $key  = $user->api_key;
        $secret  = $user->api_secret;
        $uri='https://bittrex.com/api/v1.1/account/getbalances?apikey='.$key.'&nonce='.$nonce;
        $sign=hash_hmac('sha512', $uri, $secret);
        $ch = curl_init($uri);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('apisign:'.$sign));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $execResult = curl_exec($ch);
        $obj = json_decode($execResult, true);
        $result = $obj["success"];
        return $result;
    }

    public function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }


}
