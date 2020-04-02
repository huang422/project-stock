import requests
import pandas as pd
import json
import time
#單筆資料爬蟲


#空資料
# stock = 4416
stock = 2330


#我們要請求的網址
url= "https://mops.twse.com.tw/mops/web/ajax_t100sb07_1"

#打包成發送請求
r = requests.get(url, {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'TYPEK':'all',
        'co_id':stock,
    })

r.encoding = 'utf8'

#pandas解析table
dfs = pd.read_html(r.text, header=None)


#重組資料
Data=[]

#欄位第一筆
Data += [{"0 股票代碼:":str(stock)}]

#欄位其他筆for迴圈產生
for vel,index in enumerate(dfs[0][1]):

    #判斷是不是簡報
    if (index == '法人說明會簡報內容'):
        #是的話將
        Data[0][str(vel+1)+' '+index+':'] = "https://mops.twse.com.tw/nas/STR/"+str(dfs[0][3][vel])
    else:
        Data[0][str(vel+1)+' '+index] = str(dfs[0][3][vel])


#打包成json
with open('./public/python/concall/concall.json', 'w', encoding='utf-8') as f:
    json.dump(Data, f)

print(Data)


