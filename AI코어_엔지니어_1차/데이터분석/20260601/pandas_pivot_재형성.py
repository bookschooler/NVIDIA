import numpy as np
import pandas as pd


pvdf = pd.read_excel("teacher_list_pivot_exam_1.xlsx")
print(pvdf)
# DF 재형성  메서드 ==> pivot
pvdf = pvdf.pivot(index='과정명',columns='강사명',values='강의시수')#,aggfunc="sum")
print(pvdf)
# 재형성 시점에서 해당 위치의 중복데이터가 발생할때 에러가 남 ( pivot의 단점 )
# ==> pivot_table() ==> 재형성과 동시에 중복데이터를 집계(통계)를 적용해서 형성

# 과정명 인덱스를 C , EmbC, EmbP, Linux 로 변경 하시고
print(pvdf.index)
pvdf.index = ['C','EmbC','EmbP','Linux']
print(pvdf)
# 해당 Dataframe을 막대 차트 시각화

