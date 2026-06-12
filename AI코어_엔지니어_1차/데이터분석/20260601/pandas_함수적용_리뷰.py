
import numpy as np
import pandas as pd

tipdf = pd.read_csv("tips.csv")  # csv파일을 읽어서 Dataframe 객체로 생성
#print(tipdf)
tipdf.info()

# 특정 컬럼데이터 속성이 뭐가 있고 몇개가 있는지 체크할때 ==> unique()
print(tipdf['gender'].unique())
# 새로 생성된 Series 데이터를 기존 데이터에 업데이트 시켜줘야 함
tipdf['gender'] = tipdf['gender'].map({'Female':1,'Male':0})
print(tipdf.head())
# 'total_bill' 컬럼 데이터 기준 상위 5개만 추출 ?
# 특정 컬럼데이터 기준 정렬 ==> sort_values
# by=  : 정렬할 기준 컬럼
# ascending =  : 오름차순, 내림차순 정렬 결정
tipdf.sort_values(by=['total_bill','tip'],ascending=False, inplace=True)

tipdf_top5 = tipdf.head(5).copy()
print(tipdf_top5)

# 특정 컬럼데이터의  데이터항목의 개수를 파악?
daycnt = tipdf['day'].value_counts()
print(daycnt)
daycntdf = pd.DataFrame(daycnt)
print(daycntdf)

print('='*80)
print(tipdf)
# time 컬럼의 데이터가 Lunch 인 행만 추출  ==> isin() : 불린배열
print( tipdf['time'].isin(['Lunch']) )
subset = tipdf.loc[ tipdf['time'].isin(['Lunch']), 'tip':'time' ]
print(subset)