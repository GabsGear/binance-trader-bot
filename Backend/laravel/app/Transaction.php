<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Transaction extends Model
{
 	protected $table = 'transactions';

 	protected $fillable = [
 		'tipo',
 		'bot_id', 
 		'buy_value', 
 		'quantity',
 		'sell_value',
 		'selled',
 	];
}

?>