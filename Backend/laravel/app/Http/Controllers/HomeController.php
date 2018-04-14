<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Bot;
use Auth;
use App\Http\Controllers\BotController;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function dashboard() {
        return view('dashboard');
    }

    public function reportsopen() {
        return view('reportsopen');
    }

    public function reportsclose() {
        return view('reportsclose');
    }

    public function account() {
        return view('account');
    }

    public function indicator($id) {
        $bot = Bot::find($id);
        if(Auth::user()->id != $bot->user_id)
            return redirect()->route('dashboard');
        return view('indicator', compact('bot'));
    }


}
