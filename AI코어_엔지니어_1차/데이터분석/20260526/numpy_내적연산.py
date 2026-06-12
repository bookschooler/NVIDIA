import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array( [ [2,3],[1,2] ] )
print(x)
y = np.array( [ [1,2],[2,3] ] )
print(y)
print( np.dot(x, y) )

arr1 = np.random.randint(1,13,(3,4))
print(arr1 > 6 )  #  불린배열을 형성


# 집계(통계) 함수

arr2 = np.arange(1, 50, 2).reshape((5,5))
print( arr2 )

# df = pd.DataFrame( arr2 , columns=list('abcde') )  # 넘파이 배열을 이용해서 DataFrame 객체를 생성
# print(df)
# print(df.iloc[1,2])

# # axis = 0  ( 행축 )
# # axis = 1   ( 열축 )
# print( arr2.mean(axis=0) )
# print( np.sum(arr2) )
# print( arr2.max(axis=0) )
#
# print( sum( [3,4,5,6] ) )