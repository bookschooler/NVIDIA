
import numpy as np
import pandas as pd

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

tipdf = pd.read_csv('tips.csv')
print(tipdf)
# tips.csv  파일을  읽어서
# gender 컬럼의 'Male' 을 0 으로 'Female'을 1로 일괄 변경 시켜주세요
print(tipdf['gender'].unique())
tipdf['gender'] = tipdf['gender'].map( {'Male':0, 'Female':1} )
print(tipdf)
# day 컬럼 데이터중 몇개의 요일이 있는지 체크해주세요
print(tipdf.columns)
print(tipdf['day'].unique())
print("="*80)
tipdf.info()
# 요일이 'Sat' 와 'Thur' 인 항목만 추출 출력
subset = tipdf.loc[ tipdf['day'].isin(['Sat','Thur']) , : ].copy()
print(subset)
# 토요일과 목요일의 테이블 인원수의 평균은?
# size 컬럼의 평균 계산
print( subset['tip'].mean() )

