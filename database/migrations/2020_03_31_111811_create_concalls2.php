<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateConcalls2 extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('concalls2', function (Blueprint $table) {
#sqlStuff = "INSERT INTO concalls2(stock_id,date,location,
#import_info,chinese_file,chinese_href,english_file,english_href,info,video,other) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


            $table->id();
            $table->string('stock_id', 255);
            $table->string('date', 255)->nullable();
            $table->string('location', 255)->nullable();
            $table->string('import_info', 255)->nullable();
            $table->string('chinese_file', 255)->nullable();
            $table->string('chinese_href', 255)->nullable();
            $table->string('english_file', 255)->nullable();
            $table->string('english_href', 255)->nullable();
            $table->string('info', 255)->nullable();
            $table->string('preferred_stock', 255)->nullable();
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
        Schema::dropIfExists('concalls2');
    }
}
