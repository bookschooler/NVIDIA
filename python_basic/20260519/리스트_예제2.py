listdata1 = [50, 30, 20]
# 시퀀스 객체에 지원하는 영상
# +, *, [ : ]

listdata2 = [77, 88, 99]

result = listdata1+listdata2
print(result)
print(result[1:4])

# listtmp = [None] * 10
# print(listtmp)
# listtmp[0] = 40
# print(listtmp)

listdata3 = [5,6,7,8]    # 객체 달라서 연산 불가
# print(listdata3)

listdata4 = []
for item in listdata3:
    listdata4.append(item+3)
print(listdata4)

#라이브러리 혹은 패키지 추가 문법
import numpy as np
import pandas as pd
import seaborn as sns

arr1 = np.array([99,22,33,55])
print(arr1, type(arr1))