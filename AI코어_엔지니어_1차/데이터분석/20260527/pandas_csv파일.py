
import numpy as np
import pandas as pd
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

passdf = pd.read_csv("서울특별시_지하철 승하차 승객수.csv", encoding="CP949")
#print(passdf)
passdf.info()
#print(passdf.head())
passdf['기준_날짜'] = pd.to_datetime( passdf['기준_날짜'] )  # 문자열 항목 --> 시계열 데이터  바꿔라
#print(passdf['기준_날짜'])
passdf.info()
#print(passdf.head())
passdf.set_index('기준_날짜', inplace=True)
print(passdf.head())
print("="*80)
print(passdf.loc['2025'])
print("="*80)

mydf = pd.DataFrame( np.arange(30,60) , columns=['데이터'], index= pd.date_range('2025.12.25',periods=30,freq='D'))
# index_data = pd.date_range('2025.12.25',periods=30,freq='D')  # 시계열의 범위 데이터를 생성
# print(index_data)
print(mydf)
print(mydf.loc['2026'])