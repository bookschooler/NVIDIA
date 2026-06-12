import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현

tipdf = pd.read_csv("tips.csv")
print(tipdf.head())
tipdf.info()
# ‘day’ 컬럼을 기준으로 그룹화 후‘tip‘컬럼의 데이터 합 계산 ( pivot_table )
pvdf = tipdf.pivot_table(index='day', values=['total_bill','tip'], aggfunc='sum')
print(pvdf)
fig, axes = plt.subplots(2,1, figsize=(10,6))

pvdf.plot.bar(ax=axes[0])
pvdf.plot.barh(ax=axes[1],stacked=True)  # pandas 막대차트 랜더링
plt.show()
# pvdf.reset_index(inplace=True)
# print(pvdf)
# print(pvdf['day'])
# print(pvdf['tip'])
# plt.barh(pvdf['day'], pvdf['tip']) # matplotlib 막대차트 랜더링
# plt.show()