import numpy as np
import pandas as pd
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

df = pd.read_excel('salesfunnel.xlsx')
print(df.columns)

pvdf = df.pivot_table(index=['Manager','Rep','Product'],
                      values=['Price','Quantity'] , aggfunc=['sum','mean'], margins=True )

print(pvdf)
print(pvdf.index)
print(pvdf.columns)
# 멀티컬럼을 단일 컬럼으로 변경
pvdf.columns = [ 'sum_price','sum_quantity', 'mean_price','mean_quantity']
print(pvdf)