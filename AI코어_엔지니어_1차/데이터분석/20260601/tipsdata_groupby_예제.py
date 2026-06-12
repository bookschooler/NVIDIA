import numpy as np
import pandas as pd

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

tipdf = pd.read_csv("tips.csv")  # csv파일을 읽어서 Dataframe 객체로 생성
print(tipdf)

# 그룹핑할 기준키는  'smoker'
# 집계(통계) 적용할 컬럼은 'total_bill', 'tip'
# 집계 통계 함수는 mean
#==> 흡연자,  비흡연자의 'total_bill' 과 'tip'  평균을 계산!!

grpdf = tipdf.groupby('smoker')[ ['total_bill','tip'] ].mean()
print(grpdf)


# 요일별 흡연자/비흡연자  tip 의 평균을 계산해서 출력?
# 결과는 데이터프레임으로
grpdf = tipdf.groupby(['day','smoker'])[['tip']].agg('mean')
print(grpdf)
print(grpdf.index)

print( grpdf.loc[  ( 'Sat', 'Yes') , 'tip' ] )

unstacked = grpdf.unstack()
print(unstacked)
print(unstacked.columns)

print( unstacked.loc[ 'Sun', ('tip', 'Yes') ])