import requests   #發送請求
import pandas as pd   #解析表格
import json  #打包json
import time  #延遲執行


#要爬的股票代碼
stock = ["4161 ", "4162 ", "4163 ", "4164 ", "4167 ", "4168 ", "4171 ", "4173 ", "4174 ", "4175 ", "4183 ", "4188 ", "4190 ", "4192 ", "4198 ", "4205 ", "4207 ", "4303 ", "4304 ", "4305 ", "4306 ", "4401 ", "4402 ", "4406 ", "4413 ", "4414 ", "4416 ", "4417 ", "4419 ", "4420 ", "4426 ", "4429 ", "4430 ", "4432 ", "4433 ", "4438 ", "4439 ", "4502 ", "4503 ", "4506 ", "4510 ", "4513 ", "4523 ", "4526 ", "4527 ", "4528 ", "4529 ", "4530 ", "4532 ", "4533 ", "4534 ", "4535 ", "4536 ", "4538 ", "4540 ", "4541 ", "4542 ", "4543 ", "4545 ", "4549 ", "4550 ", "4551 ", "4552 ", "4554 ", "4555 ", "4556 ", "4557 ", "4560 ", "4561 ", "4562 ", "4563 ", "4564 ", "4566 ", "4568 ", "4571 ", "4572 ", "4576 ", "4580 ", "4609 ", "4702 ", "4706 ", "4707 ", "4711 ", "4712 ", "4714 ", "4716 ", "4720 ", "4721 ", "4722 ", "4725 ", "4726 ", "4728 ", "4729 ", "4735 ", "4736 ", "4737 ", "4739 ", "4741 ", "4743 ", "4744 ", "4745 ", "4746 ", "4747 ", "4754 ", "4755 ", "4760 ", "4763 ", "4764 ", "4766 ", "4767 ", "4803 ", "4804 ", "4806 ", "4807 ", "4903 ", "4904 ", "4905 ", "4906 ", "4907 ", "4908 ", "4909 ", "4911 ", "4912 ", "4915 ", "4916 ", "4919 ", "4924 ", "4927 ", "4930 ", "4931 ", "4933 ", "4934 ", "4935 ", "4938 ", "4939 ", "4942 ", "4943 ", "4944 ", "4946 ", "4947 ", "4950 ", "4952 ", "4953 ", "4956 ", "4958 ", "4960 ", "4961 ", "4966 ", "4967 ", "4968 ", "4971 ", "4972 ", "4973 ", "4974 ", "4976 ", "4977 ", "4979 ", "4987 ", "4989 ", "4991 ", "4994 ", "4995 ", "4999 ", "5007 ", "5009 ", "5011 ", "5013 ", "5014 ", "5015 ", "5016 ", "5102 ", "5201 ", "5202 ", "5203 ", "5205 ", "5206 ", "5209 ", "5210 ", "5211 ", "5212 ", "5213 ", "5215 ", "5220 ", "5223 ", "5225 ", "5227 ", "5230 ", "5234 ", "5243 ", "5245 ", "5251 ", "5258 ", "5263 ", "5264 ", "5269 ", "5272 ", "5274 ", "5276 ", "5278 ", "5281 ", "5283 ", "5284 ", "5285 ", "5287 ", "5288 ", "5289 ", "5291 ", "5299 ", "5301 ", "5302 ", "5304 ", "5305 ", "5306 ", "5309 ", "5310 ", "5312 ", "5314 ", "5315 ", "5321 ", "5324 ", "5328 ", "5340 ", "5344 ", "5345 ", "5347 ", "5348 ", "5349 ", "5351 ", "5353 ", "5355 ", "5356 ", "5364 ", "5371 ", "5381 ", "5383 ", "5386 ", "5388 ", "5392 ", "5398 ", "5403 ", "5410 ", "5425 ", "5426 ", "5432 ", "5434 ", "5438 ", "5439 ", "5443 ", "5450 ", "5452 ", "5455 ", "5457 ", "5460 ", "5464 ", "5465 ", "5468 ", "5469 ", "5471 ", "5474 ", "5475 ", "5478 ", "5481 ", "5483 ", "5484 ", "5487 ", "5488 ", "5489 ", "5490 ", "5493 ", "5498 ", "5508 ", "5511 ", "5512 ", "5514 ", "5515 ", "5516 ", "5519 ", "5520 ", "5521 ", "5522 ", "5523 ", "5525 ", "5529 ", "5530 ", "5531 ", "5533 ", "5534 ", "5536 ", "5538 ", "5543 ", "5601 ", "5603 ", "5604 ", "5607 ", "5608 ", "5609 ", "5701 ", "5703 ", "5704 ", "5706 ", "5820 ", "5864 ", "5871 ", "5876 ", "5878 ", "5880 ", "5902 ", "5903 ", "5904 ", "5905 ", "5906 ", "5907 ", "6005 ", "6015 ", "6016 ", "6020 ", "6021 ", "6023 ", "6024 ", "6026 ", "6101 ", "6103 ", "6104 ", "6108 ", "6109 ", "6111 ", "6112 ", "6113 ", "6114 ", "6115 ", "6116 ", "6117 ", "6118 ", "6120 ", "6121 ", "6122 ", "6123 ", "6124 ", "6125 ", "6126 ", "6127 ", "6128 ", "6129 ", "6130 ", "6131 ", "6133 ", "6134 ", "6136 ", "6138 ", "6139 ", "6140 ", "6141 ", "6142 ", "6143 ", "6144 ", "6146 ", "6147 ", "6148 ", "6150 ", "6151 ", "6152 ", "6153 ", "6154 ", "6155 ", "6156 ", "6158 ", "6160 ", "6161 ", "6163 ", "6164 ", "6165 ", "6166 ", "6167 ", "6168 ", "6169 ", "6170 ", "6171 ", "6172 ", "6173 ", "6174 ", "6175 ", "6176 ", "6177 ", "6179 ", "6180 ", "6182 ", "6183 ", "6184 ", "6185 ", "6186 ", "6187 ", "6188 ", "6189 ", "6190 ", "6191 ", "6192 ", "6194 ", "6195 ", "6196 ", "6197 ", "6198 ", "6199 ", "6201 ", "6202 ", "6203 ", "6204 ", "6205 ", "6206 ", "6207 ", "6208 ", "6209 ", "6210 ", "6212 ", "6213 ", "6214 ", "6215 ", "6216 ", "6217 ", "6218 ", "6219 ", "6220 ", "6221 ", "6222 ", "6223 ", "6224 ", "6225 ", "6226 ", "6227 ", "6228 ", "6229 ", "6230 ", "6231 ", "6233 ", "6234 ", "6235 ", "6236 ", "6237 ", "6238 ", "6239 ", "6240 ", "6241 ", "6242 ", "6243 ", "6244 ", "6245 ", "6246 ", "6247 ", "6248 ", "6251 ", "6257 ", "6259 ", "6261 ", "6263 ", "6264 ", "6265 ", "6266 ", "6269 ", "6270 ", "6271 ", "6274 ", "6275 ", "6276 ", "6277 ", "6278 ", "6279 ", "6281 ", "6282 ", "6283 ", "6284 ", "6285 ", "6287 ", "6288 ", "6289 ", "6290 ", "6291 ", "6292 ", "6294 ", "6404 ", "6405 ", "6409 ", "6411 ", "6412 ", "6414 ", "6415 ", "6416 ", "6417 ", "6418 ", "6419 ", "6425 ", "6426 ", "6431 ", "6432 ", "6435 ", "6438 ", "6441 ", "6442 ", "6443 ", "6446 ", "6449 ", "6451 ", "6452 ", "6456 ", "6457 ", "6461 ", "6462 ", "6464 ", "6465 ", "6469 ", "6470 ", "6472 ", "6477 ", "6482 ", "6485 ", "6486 ", "6488 ", "6491 ", "6492 ", "6494 ", "6496 ", "6497 ", "6499 ", "6504 ", "6505 ", "6506 ", "6508 ", "6509 ", "6510 ", "6512 ", "6514 ", "6516 ", "6523 ", "6525 ", "6527 ", "6530 ", "6531 ", "6532 ", "6533 ", "6535 ", "6538 ", "6541 ", "6542 ", "6547 ", "6548 ", "6552 ", "6556 ", "6558 ", "6560 ", "6561 ", "6568 ", "6569 ", "6570 ", "6573 ", "6574 ", "6576 ", "6577 ", "6578 ", "6579 ", "6581 ", "6582 ", "6589 ", "6590 ", "6591 ", "6592 ", "6593 ", "6594 ", "6596 ", "6603 ", "6605 ", "6609 ", "6612 ", "6613 ", "6615 ", "6616 ", "6624 ", "6625 ", "6629 ", "6640 ", "6641 ", "6642 ", "6643 ", "6649 ", "6654 ", "6655 ", "6662 ", "6664 ", "6666 ", "6667 ", "6668 ", "6669 ", "6670 ", "6671 ", "6672 ", "6674 ", "6679 ", "6680 ", "6683 ", "6690 ", "6697 ", "6698 ", "6706 ", "6715 ", "6803 ", "7402 ", "8011 ", "8016 ", "8021 ", "8024 ", "8027 ", "8028 ", "8032 ", "8033 ", "8034 ", "8038 ", "8039 ", "8040 ", "8042 ", "8043 ", "8044 ", "8046 ", "8047 ", "8048 ", "8049 ", "8050 ", "8054 ", "8059 ", "8064 ", "8066 ", "8067 ", "8068 ", "8069 ", "8070 ", "8071 ", "8072 ", "8074 ", "8076 ", "8077 ", "8080 ", "8081 ", "8083 ", "8084 ", "8085 ", "8086 ", "8087 ", "8088 ", "8091 ", "8092 ", "8093 ", "8096 ", "8097 ", "8099 ", "8101 ", "8103 ", "8104 ", "8105 ", "8107 ", "8109 ", "8110 ", "8111 ", "8112 ", "8114 ", "8121 ", "8131 ", "8147 ", "8150 ", "8155 ", "8163 ", "8171 ", "8176 ", "8182 ", "8183 ", "8201 ", "8210 ", "8213 ", "8215 ", "8222 ", "8234 ", "8240 ", "8249 ", "8255 ", "8261 ", "8271 ", "8277 ", "8279 ", "8287 ", "8289 ", "8291 ", "8299 ", "8341 ", "8342 ", "8349 ", "8354 ", "8358 ", "8367 ", "8374 ", "8383 ", "8390 ", "8401 ", "8403 ", "8404 ", "8406 ", "8409 ", "8410 ", "8411 ", "8415 ", "8416 ", "8418 ", "8420 ", "8421 ", "8422 ", "8423 ", "8424 ", "8426 ", "8427 ", "8429 ", "8431 ", "8432 ", "8433 ", "8435 ", "8436 ", "8437 ", "8440 ", "8442 ", "8443 ", "8444 ", "8446 ", "8450 ", "8454 ", "8455 ", "8462 ", "8463 ", "8464 ", "8466 ", "8467 ", "8472 ", "8473 ", "8476 ", "8477 ", "8478 ", "8480 ", "8481 ", "8482 ", "8488 ", "8489 ", "8497 ", "8499 ", "8905 ", "8906 ", "8908 ", "8916 ", "8917 ", "8921 ", "8923 ", "8924 ", "8926 ", "8927 ", "8928 ", "8929 ", "8930 ", "8931 ", "8932 ", "8933 ", "8934 ", "8935 ", "8936 ", "8937 ", "8938 ", "8940 ", "8941 ", "8942 ", "8996 ", "9103 ", "91032", "91048", "9105 ", "91086", "9110 ", "91160", "91161", "91162", "91186", "91200", "91239", "9136 ", "9188 ", "9802 ", "9902 ", "9904 ", "9905 ", "9906 ", "9907 ", "9908 ", "9910 ", "9911 ", "9912 ", "9914 ", "9917 ", "9918 ", "9919 ", "9921 ", "9924 ", "9925 ", "9926 ", "9927 ", "9928 ", "9929 ", "9930 ", "9931 ", "9933 ", "9934 ", "9935 ", "9937 ", "9938 ", "9939 ", "9940 ", "9941 ", "9942 ", "9943 ", "9944 ", "9945 ", "9946 ", "9949 ", "9950 ", "9951 ", "9955 ", "9958 ", "9960 ", "9962 " ]



#多筆資料爬蟲


Data=[]
#定義function
#直譯式語言
#重組資料
def ReORG():
    for vel,index in enumerate(dfs[0][1]):
        if (index == '法人說明會簡報內容'):
            Data[stockVar][str(vel+1)+' '+index+':'] = "https://mops.twse.com.tw/nas/STR/"+str(dfs[0][3][vel])
        else:
            Data[stockVar][str(vel+1)+' '+index] = str(dfs[0][3][vel])

#for迴圈去重複爬取
for stockVar,index in enumerate(stock):
    x = stockVar+1
    print('************************')
    print(x,' ',index,'讀取中')

    url= "https://mops.twse.com.tw/mops/web/ajax_t100sb07_1"

    #發送請求
    r = requests.get(url, {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'TYPEK':'all',
        'co_id':index,
    })
    r.encoding = 'utf8'


    try:
        dfs = pd.read_html(r.text, header=None)
    except ValueError as n:
        try:
            print(x,' ',index,'空的啦')
            Data += [{"0 股票代碼:":str(index)}]
        except KeyError as n:
            print(x,' ',index,'太快啦')
            time.sleep(60)
            r = requests.get(url, {
                'encodeURIComponent':1,
                'step':1,
                'firstin':1,
                'off':1,
                'TYPEK':'all',
                'co_id':index,
            })
            r.encoding = 'utf8'
            dfs = pd.read_html(r.text, header=None)
            Data += [{"0 股票代碼:":str(index)}]
    else:
        try:
            Data += [{"0 股票代碼:":str(index)}]
            ReORG()
        except KeyError as n:
            print(x,' ',index,'太快啦')
            time.sleep(60)
            r = requests.get(url, {
                'encodeURIComponent':1,
                'step':1,
                'firstin':1,
                'off':1,
                'TYPEK':'all',
                'co_id':index,
            })
            r.encoding = 'utf8'
            try:
                dfs = pd.read_html(r.text, header=None)
            except ValueError as n:
                print(x,' ',index,'空的啦')
                Data += [{"0 股票代碼:":str(index)}]
            else:
                Data += [{"0 股票代碼:":str(index)}]
                ReORG()
                print(x,' ',index,'過了過了')
                with open('./public/python/concall/concall.json', 'w',encoding='utf-8') as f:
                    json.dump(Data, f)

        else:
            print(x,' ',index,'過了過了')
            with open('./public/python/concall/concall.json', 'w',encoding='utf-8') as f:
                json.dump(Data, f)




print("ok")

