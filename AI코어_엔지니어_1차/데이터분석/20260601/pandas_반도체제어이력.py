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

df = pd.read_excel('반도체_제어_이력.xlsx')
print(df.info())
print(df.columns)
# '공정 단계', '장비명', '파라미터', '목표값', '실제값'  5개 컬럼만 선택 추출
semidf = df[ ['공정 단계', '장비명', '파라미터', '목표값', '실제값'] ].copy()
print(semidf)

# 1 문제)  장비명에 숫자문자가 있는 장비명 행만 추출(선택)
import re
# def DeviceCheck(arg):
#     if len( re.findall(r'[0-9]+', arg) ) > 0:
#         return True
#     else:
#         return False

# subset = semidf.loc[ semidf['장비명'].apply(DeviceCheck), : ].copy()
# print(subset)

subset = semidf.loc[ semidf['장비명'].apply(lambda x: True  if len( re.findall(r'[0-9]+', x) ) > 0 else False ), : ].copy()
print(subset)

# 2 문제) 공정단계중 가장많은 공정단계는 뭔가요?
print(semidf['공정 단계'].value_counts())

print('='*80)
print(semidf)
# 공정 단계별 목표값, 실제값의 평균을 계산해서 출력 ( 그룹핑 )?

grp = semidf.groupby('공정 단계')[['목표값','실제값']].mean()
print(grp)

grp.plot.bar()  #  DF 막대그래프 랜더링
plt.show()