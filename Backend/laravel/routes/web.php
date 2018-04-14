<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::group(['middleware' => ['auth']], function() {
	Route::auth();
	//GET MENU ROUTES
	Route::get('/dashboard', 'HomeController@dashboard')->name('dashboard');
	Route::get('/reports/open', 'HomeController@reportsopen')->name('reports.open');
	Route::get('/reports/close', 'HomeController@reportsclose')->name('reports.close');
	Route::get('/account', 'HomeController@account')->name('account');
	Route::get('/indicator/{id}', 'HomeController@indicator')->name('indicator');
	Route::get('/mail', 'EmailController@send')->name('email');
	//GET BOT ROUTES
	Route::get('/bot/view/{id}', 'BotController@view')->name('bot.view');
	Route::get('/bot/active/{id}', 'BotController@active')->name('bot.active');
	Route::get('/bot/stop/{id}', 'BotController@stop')->name('bot.stop');
	Route::delete('/bot/destroy/{id}', 'BotController@destroy')->name('bot.destroy');
	Route::get('/dashboard/stopall', 'BotController@stopAll')->name('bot.stopall');
	Route::get('/bot/candles/{id}', 'BotController@getCandles')->name('bot.candles');
	Route::get('/bot/trans/{id}', 'TransactionController@getTrans')->name('bot.trans');

	Route::post('/dashboard', [ 'as' => 'bot.create', 'uses' => 'BotController@create']);
	Route::post('/bot/updateperiod/{id}', 'BotController@changePeriod')->name('bot.period');
	Route::post('/bot/update/{id}', 'BotController@update')->name('bot.update');
	Route::post('/bot/updatewallet/{id}', 'BotController@updateWallet')->name('bot.updatewallet');

	## ACC POST ROUTES	
	Route::post('/account/update', 'UserController@updateAPI')->name('acc.updateapi');
	Route::post('/account/changepass', 'UserController@reset')->name('acc.changepass');
	Route::post('/account/logout', 'UserController@logout')->name('acc.logout');

});

Route::get('/botstatus', 'BotController@botsstatus')->name('botstatus');

Route::get('password/reset/{token}', 'Auth\ForgotPasswordController@getReset')->name('forgotpass.get');
Route::post('password/reset', 'Auth\ForgotPasswordController@postReset')->name('forgotpass.form');

Route::get('forgotpassword', 'EmailController@getEmailForgotPass')->name('email.password.get');
Route::post('forgotpassword', 'EmailController@postEmailForgotPass')->name('email.password.post');


Route::get('/register', function () { 
	return view('register'); 
});

Route::get('/',array('as'=>'login', function(){ 
	return view('login'); 
}));

Route::post('/register', 'Auth\RegisterController@create')->name('register');
Route::post('/login', 'Auth\LoginController@login')->name('customlogin');
