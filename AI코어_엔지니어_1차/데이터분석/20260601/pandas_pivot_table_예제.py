import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

tipdf = pd.read_csv("tips.csv")  # csv파일을 읽어서 Dataframe 객체로 생성
print(tipdf)
# 요일별 'total_bill', 'tip' 의 총합을 계산 출력
grp = tipdf.groupby('day')[['total_bill','tip']].agg('sum')
print(grp)

# 재형성에서 pivot_table()
pvdf = tipdf.pivot_table(index='day', values=['total_bill','tip'], aggfunc='sum')
print(pvdf)

pvdf = tipdf.pivot_table(index='day',columns='smoker', values='tip', aggfunc='sum')
print(pvdf)
#  smoker  No   Yes
#  day
#  Fri   11.25    40.71
#  Sat   139.63   120.77
#  Sun   180.57   66.82
#  Thur  120.32   51.51
# 막대그래프로 시각화
pvdf.plot.bar(stacked=True, rot = 15) # stacked=True ==> 누적차트
plt.show()