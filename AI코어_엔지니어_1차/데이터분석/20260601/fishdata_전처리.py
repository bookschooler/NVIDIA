import numpy as np
import pandas as pd
import seaborn as sns  # seaborn 라이브러리 이용한 시각화
import matplotlib.pyplot as plt  # 차트 시각화 라이브러리(패키지)
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

fishdf = pd.read_csv('Fish.csv')
#print(fishdf.head())
del fishdf['Length2']
del fishdf['Length3']
fishdf.rename(columns={'Length1':'Length'}, inplace=True)
print(fishdf.head())

# 각 종별 Height, Width의 평균을 계산해서 출력
pvdf = fishdf.pivot_table(index='Species', values=['Height','Width'], aggfunc='mean')
print(pvdf)

# Height, Width 각 컬럼별 평균에 5씩 일괄 증가
# ==> 함수적용방법을 활용하되 lambda 함수(표현식)을 활용

# pvdf['Height'] = pvdf['Height'].apply(lambda x, y: x+5)
# pvdf['Width'] = pvdf['Width'].apply(lambda x : x+5)

pvdf = pvdf.map(lambda x : x+5)
print(pvdf)


# 몇 종류에 물고기 있나요?
# print(fishdf['Species'].unique())
# print(fishdf.head())
# fishdf = fishdf[['Species','Weight','Length1']].copy()
# #print(fishdf)
# fishdf.rename(columns={'Length1':'Length'}, inplace=True)
# print(fishdf.head())
# #
# # # plt.scatter() # 산점도
# # # x 축을 Length
# # # y 축을 Weight 로 설정해서 산점도 출력
# # plt.scatter(x=fishdf['Length'], y=fishdf['Weight'])
# # plt.show()
#
# sns.lmplot(data=fishdf, x='Length', y='Weight',
#            hue='Species',fit_reg=False)
#
# plt.show()