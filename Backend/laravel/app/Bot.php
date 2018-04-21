<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Bot extends Model
{
 	protected $table = 'bot';

 	protected $fillable = [
 			'user_id',
 			'exchange',
 			'currency', 
 			
 			'strategy_buy', 
 			'strategy_sell', 
 			'percentage', 

 			'pid', ##PID DO PROCESSO EM EXECUÇÃO | INT
 			'active', ## 0: MODO DE SIMULAÇÃO | 1: MODO REAL FUNCIONAL | INT
 			'max_order',  ##NUMERO MAXIMO DE ORDENS DE COMPRA QUE O BOT PODE EXECUTAR | INT
 			'order_value', ##VALOR DAS ORDENS DE COMPRA | FLOAT
 			'period', ##TEMPO GRÁFICO DO BOT | STRING
 			'stoploss',  ##STOP LOSS
 	];
}

?>
