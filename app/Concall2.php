<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Concall2 extends Model
{
    //
    protected $table ='concalls2';

    protected $fillable = [
        'stock_id',
        'date',
        'location',
        'import_info',
        'chinese_file',
        'chinese_href',
        'english_file',
        'english_href',
        'info',
        'video',
        'other',

    ];
}
