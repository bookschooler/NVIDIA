import numpy as np
import pandas as pd
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

passdf = pd.read_csv("서울특별시_지하철 승하차 승객수.csv", encoding="CP949")
print(passdf)
#passdf.info()
# 호선_명칭 기준 ==> 3호선 , 7호선, 9호선, 수인선 만 추출
print( passdf['호선_명칭'].unique())

print( passdf['호선_명칭'].isin(['3호선','7호선','9호선','수인선']) )  # 있으면 True, 없으면 False
print('='*80)
subset = passdf.loc[  passdf['호선_명칭'].isin(['3호선','7호선','9호선','수인선']) , : ]
print(subset)
# print( passdf['호선_명칭'] == '3호선' )  # 불린배열
# subset1 = passdf.loc[ passdf['호선_명칭'] == '3호선' ,  : ].copy()
# print(subset1)
# subset2 = passdf.loc[ passdf['호선_명칭'] == '9호선' ,  : ].copy()
# print(subset2)
#
# condf = pd.concat([subset1, subset2])
# print(condf)