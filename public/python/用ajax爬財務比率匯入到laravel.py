import sys
import json
import pandas as pd
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


url="https://mops.twse.com.tw/mops/web/ajax_t05st22"

r = requests.get(url, {
        'encodeURIComponent':1,
        'run':'Y',
        'step':1,
        'TYPEK':'all',
        'year':108,
        'isnew':True,
        'co_id':int(sys.argv[1]),    #int(sys.argv[1])
        'firstin':1,
        'off':1,
        'ifrs':'Y'
    })


# print(r.text)
r.encoding = 'utf8'
dfs = pd.read_html(r.text, header=None)
financedata=dfs[len(dfs)-1].iloc[:,2:5]

##把nan轉成null
financedata2 = financedata.where(pd.notnull(financedata),'null')


#將dataframe轉成list
finance=financedata2.values.tolist()


year =financedata.columns.tolist()

#財務結構
Financialstructure_dict = {
             #time還要改
             "time": year,
             #負債佔資產比率(%)
             "debtratio": finance[0],
             #長期資金佔不動產、廠房及設備比率(%)
             "Long_term_to_fixedassets":  finance[1]

                }




#償債能力
Debtrepayment_dict = {
             #time還要改
             "time": year,
             "currentratio": finance[2],
             #速動比率(%)
             "quickratio": finance[3],
              #利息保障倍數(%)
             "interestcoverageratio": finance[4]

                }


#經營能力
management_dict = {
             #time還要改
             "time": year,
             #應收款項週轉率(次)
             "RTR": finance[5],
             #平均收現日數
             "ACD": finance[6],
              #存貨週轉率(次)
             "ITR": finance[7],
              #平均銷貨日數
             "ASD": finance[8],
              #不動產、廠房及設備週轉率(次)
             "TRR": finance[9],
             #總資產週轉率(次)
             "TROTA": finance[10]
                }




#獲利能力
profit_dict = {
             #time還要改
             "time": year,
             #資產報酬率(%)
             "ROA": finance[11],
             #權益報酬率(%)
             "ROE": finance[12],
             #稅前純益佔實收資本比率(%)
             "NPBF" : finance[13],
              #純益率(%)
             "NPM" : finance[14],
              #每股盈餘(元)
             "EPS": finance[15]

                }


#現金流量
cash_dict = {
             #time還要改
             "time": year,
             #現金流量比率(%)
             "CFA": finance[16],
             #現金流量允當比率(%)
             "CFAR": finance[17],
             #現金再投資比率(%)
             "CRR" : finance[18]
                }

finance = [Financialstructure_dict,Debtrepayment_dict,management_dict,profit_dict,cash_dict]

finance_ratio= json.dumps(finance)
print(finance_ratio)







