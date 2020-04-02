<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateConcalls extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('concalls', function (Blueprint $table) {
            $table->id();
            $table->integer('stock_id');
            $table->string('date', 255)->nullable();
            $table->string('location', 255)->nullable();
            $table->string('import_info', 255)->nullable();
            $table->string('chinese_file', 255)->nullable();
            $table->string('chinese_href', 255)->nullable();
            $table->string('english_file', 255)->nullable();
            $table->string('english_href', 255)->nullable();
            $table->string('info', 255)->nullable();
            $table->string('video', 255)->nullable();
            $table->string('other', 255)->nullable();

        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('concalls');
    }
}
