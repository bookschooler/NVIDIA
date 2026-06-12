

# 'seoul_keumchun_gas_info.csv' 을 Dataframe 객체로 생성하고
import numpy as np
import pandas as pd

df = pd.read_csv("seoul_keumchun_gas_info.csv",encoding="CP949",index_col=0)
print(df)
df.info()
# 생성된 Dataframe 의 "데이터기준일자" 컬럼 데이터가
# datetime 이 아니고 object(문자열) 이면  datetime type으로 변환
# 변환 이후 해당 컬럼을 인덱스로 설정해줌.
# ==> 완벽한 시계열 데이터 형성
df['데이터기준일자'] = pd.to_datetime( df['데이터기준일자'] )  # 해당 컬럼 데이터를 시계열 데이터로 변환해줘
df.info()
print(df)

df.set_index('데이터기준일자', inplace=True)
print('='*80)
print(df)


