import pandas as pd
import requests
from pykrx import stock
import time


headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    }

def employee_url(code,year,time1):
    return 'https://opendart.fss.or.kr/api/empSttus.json?crtfc_key=28fbb2a7b71ecbd69bed5d2f6ca62737d6c8de9f&corp_code='+code+'&bsns_year='+year+'&reprt_code='+time1

time1 = {
    "1":"11013",
    "2":'11012',
    '3':'11014',
    '4':'11011'
}


df = pd.read_csv('kospi3.csv')

try:
    for idx in range(5064,5091):
        print(df['종목'][idx],)
        num = str(df['심볼번호'][idx]).rjust(8,'0')
        year,quater = str(df['time'][idx]).split('_')
        res = requests.get(employee_url(num,year,time1[quater]),headers=headers).json()
        time.sleep(1)
        if res['status'] == '020': 
            print(df['종목'][idx], year,quater,'api 종료')
            break
        if res['status'] == '013' : continue
        salary = []
        for list in res['list']:
            if '합계' in list['fo_bbm'] or  list['jan_salary_am'] == '-':#합계 거나 sm 이 없을때
                continue
            salary.append(int(list['jan_salary_am'].replace(',','')))
        if len(salary) != 0:
            df['avg_salary'][idx] = sum(salary)/len(salary)
            



except Exception as e:
    print(e)

finally:
    df.to_csv('kospi3.csv',encoding='utf-8-sig',mode='w', index=False)
