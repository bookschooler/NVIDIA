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


# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60,55], 'Kim':[85,95,65,55,95], 'Park':[88, 93, 75, 72,45], 'Lee':[55,66,77,92,65] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music','sci'])
print(scoredf)
# 삭제 문법
# 특정 컬럼 하나 삭제 할때 유용 ==> del 키워드
# del scoredf['Park']
# print(scoredf)

# 특정 컬럼(행) 이나 여러개의 컬럼(행)을 삭제하는 메서드 ( drop )
# inplace = True 이면 원본에 직접
# inplace = False 이면 사본객체 생성
# print("="*80)
# scoredf.drop(['Hong','Park'], axis=1, inplace=True)
# print("="*80)
# print( scoredf )

# scoredf.drop(['eng','music'], axis=0, inplace=True)
# print("="*80)
# print( scoredf )
#

print("="*80)
print( scoredf )
scoredf.index = ["국어","영어","수학","음악","과학"]
print("="*80)
print( scoredf )

scoredf.plot.bar()  # 막대차트 랜더링
plt.show()