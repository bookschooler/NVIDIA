import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현

# flightsdf = sns.load_dataset('flights')
# print(flightsdf)
# pvdf = flightsdf.pivot_table(index='year', values='passengers', aggfunc='sum')
# print(pvdf)
#
# sns.barplot(data=pvdf, x=pvdf.index, y='passengers', palette='Set3')
# plt.show()

titanicdf = sns.load_dataset('titanic')
print(titanicdf.head())
titanicdf.info()
# 'age' 성별 기준으로 결측치 행을 제거
titanicdf.dropna(subset='age',axis=0, how='any', inplace=True)
print(titanicdf.info())
# 'sex' 컬럼명을 'gender' 컬럼명으로 변경
titanicdf.rename(columns={'sex':'gender'}, inplace=True)
print(titanicdf.head())

#grp = titanicdf.groupby(['pclass','gender'])[['fare']].mean()
pvdf = titanicdf.pivot_table(index=['pclass','gender'],values='fare', aggfunc='mean')
print(pvdf)
pvdf = pvdf.unstack()
print(pvdf)
pvdf.columns = ['fare_female', 'fare_male']
print(pvdf)

pvdf.plot.bar()
plt.show()