
listdata1 = [50, 30, 20]
# 시퀀스객체에 지원하는 연산 ==> + , * , :
listdata2 = [77, 88, 99]

reslist = listdata1 + listdata2  # 하나의 리스트로 합쳐줌
print(reslist)
print(reslist[1:4])
# listtmp = [None] * 10
# print(listtmp)
# listtmp[9] = 40
# print(listtmp)

#listdata3 = [5,6,7,8] + 3  # 리스트 + 연산은 리스트 객체 끼리는 가능 ( 리스트의 한계 )
#print(listdata3)

# listdata4 = []
# for item in listdata3:
#     listdata4.append(item+3)
# print(listdata4)

# 라이브러리(패키지) 추가 하는 문법
# as : 별칭 부여 문법
import numpy as np
arr1 = np.array([9,22,33,55])
print(arr1, type(arr1))
print( arr1 + 3 )
