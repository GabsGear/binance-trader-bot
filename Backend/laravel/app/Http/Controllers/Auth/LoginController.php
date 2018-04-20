<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\AuthenticatesUsers;
use Illuminate\Http\Request;
use Auth;

class LoginController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles authenticating users for the application and
    | redirecting them to your home screen. The controller uses a trait
    | to conveniently provide its functionality to your applications.
    |
    */

    use AuthenticatesUsers;

    /**
     * Where to redirect users after login.
     *
     * @var string
     */

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    protected $redirectTo = '/dashboard';

    public function login(Request $request) {

        if(Auth::attempt(['email'=>$request->email, 'password' => $request->password])) {
            return redirect()->action('HomeController@dashboard');
        } else {
            return view('login');
        }
    }


    public function __construct()
    {
        $this->middleware('guest')->except('logout');
    }
}
