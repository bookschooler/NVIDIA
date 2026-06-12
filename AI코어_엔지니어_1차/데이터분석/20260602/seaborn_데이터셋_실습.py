import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현

tipdf = sns.load_dataset('tips')
print(tipdf.head())
tipdf.info()
print( tipdf.describe() )  # 전체 데이터중 수치 데이터 컬럼만 선별해서 기본 통계데이터를 제공
print( tipdf['total_bill'].max())



# titanicdf = sns.load_dataset('titanic')
# print(titanicdf.head())
# titanicdf.dropna(subset='age', inplace=True)
# titanicdf.info()
#
# sns.histplot(data=titanicdf, x='age', kde=True)
# plt.show()

# irisdf = sns.load_dataset('iris')
# print(irisdf.head())
# # iris 데이터를 sns lmplot으로 산점도 시각화
# # 3종류의 붓꽃을 하나의 plot창에 동시 시각화 , fig_reg = False(회귀선 False)
# # x축 ==> petal_length
# # y축 ==> petal_width
# sns.lmplot(data=irisdf, x='petal_length', y='petal_width', hue='species', fit_reg=False)
# plt.show()


# tipdf = pd.read_csv('tips.csv')
# print(tipdf.head())
#
# tipdf['tip_pct'] = tipdf['tip'] / ( tipdf['total_bill'] - tipdf['tip'])
# print(tipdf.head())
#
# sns.set_style("darkgrid")
#
# fig, axes = plt.subplots(1,2, figsize=(10,6))
#
# sns.regplot(x=tipdf['total_bill'], y=tipdf['tip'], ax=axes[0], fit_reg=True, color='orange')
# # 산점도그래프(선형회귀선미표시: fit_reg = False )
# sns.regplot(x=tipdf['total_bill'], y=tipdf['tip'], ax=axes[1], fit_reg=False, color='blue')
# plt.show()