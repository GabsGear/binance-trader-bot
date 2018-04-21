<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateBotTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('bot', function (Blueprint $table) {
            $table->increments('id');
            $table->string('currency');
            $table->float('dsvadx', 8, 3);
            $table->float('dsvbal', 8, 3);
            $table->float('dsvtop', 8, 3);
            $table->float('dsvbot', 8, 3);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('bot');
    }
}
