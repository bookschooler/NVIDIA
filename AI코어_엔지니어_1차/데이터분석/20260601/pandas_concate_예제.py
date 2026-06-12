import numpy as np
import pandas as pd

tipdf = pd.read_csv("tips.csv")  # csv파일을 읽어서 Dataframe 객체로 생성
print(tipdf)
#tipdf.info()
# 'day' 컬럼 데이터중  'Sat' , 'Fri' 데이터만 추출?

subset1 = tipdf.loc[ tipdf['day'] == 'Sat', :]
print(subset1)
subset2 = tipdf.loc[ tipdf['day'] == 'Fri', :]
print(subset2)

print('='*80)
condf = pd.concat([subset1, subset2], axis=0)
print(condf)