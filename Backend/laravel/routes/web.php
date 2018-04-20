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
	Route::delete('/bot/destroy/{id}', 'BotController@destroy')->name('bot.destroy');
	Route::get('/dashboard/stopall', 'BotController@stopAll')->name('bot.stopall');
	Route::get('/bot/trans/{id}', 'TransactionController@getTrans')->name('bot.trans');

	Route::post('/bot/active', 'BotController@active')->name('bot.active');
	Route::post('/dashboard', [ 'as' => 'bot.create', 'uses' => 'BotController@create']);
	Route::post('/bot/updatewallet/{id}', 'BotController@updateWallet')->name('bot.updatewallet');

	// TRANS POST ROUTES
	Route::post('/trans/filter/date', 'TransactionController@filter_date')->name('trans.filter.date');
	Route::post('/trans/filter/name', 'TransactionController@filter_name')->name('trans.filter.name');

	## ACC POST ROUTES	
	Route::post('/account/update/bittrex', 'UserController@update_api_bittrex')->name('acc.api.bittrex');
	Route::post('/account/update/binance', 'UserController@update_api_binance')->name('acc.api.binance');
	Route::post('/account/changepass', 'UserController@reset')->name('acc.changepass');
	Route::post('/account/logout', 'UserController@logout')->name('acc.logout');

	##PAYMENT ROUTES
	Route::get('/payment/post', 'PaymentController@listen')->name('listen');
	Route::get('/payment', function () { 
		return view('coinpayment'); 
	});

});


Route::get('password/reset/{token}', 'Auth\ForgotPasswordController@getReset')->name('forgotpass.get');
Route::post('password/reset', 'Auth\ForgotPasswordController@postReset')->name('forgotpass.form');

Route::get('forgotpassword', 'EmailController@getEmailForgotPass')->name('email.password.get');
Route::post('forgotpassword', 'EmailController@postEmailForgotPass')->name('email.password.post');


Route::get('/register', function () { 
	return view('register'); 
});

Route::get('/termos', function () { 
	return view('termos'); 
});

Route::get('/',array('as'=>'login', function(){ 
	return view('login'); 
}));

Route::post('/register', 'Auth\RegisterController@create')->name('register');
Route::post('/login', 'Auth\LoginController@login')->name('customlogin');