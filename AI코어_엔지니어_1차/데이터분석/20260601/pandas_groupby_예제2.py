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

df = pd.read_excel('국소마취제_groupby.xlsx')
print(df.info())
print(df.head(10))

# 상병명 기준으로  금액이 가장 큰 상위 top 5개만 추출
pvdf = df.pivot_table(index='상병명', values='금액', aggfunc='sum')
print(pvdf)
print(pvdf.info())
# 금액 컬럼 기준으로 내림차순 정렬
pvdf.sort_values(by='금액', ascending=False, inplace=True)
#print(pvdf)
subset = pvdf.head().copy()
print(subset)
subset.reset_index(inplace=True)
print(subset)
# seaborn 라이브러리 이용해서 막대 차트 시각화
sns.barplot(data=subset, x='상병명', y='금액', palette='Set3')
plt.show()



