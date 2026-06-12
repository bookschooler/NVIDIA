import numpy as np
import  pandas as pd

df1 = pd.DataFrame( {"customid":[1234,5678,1111,8888,3333] , 'name':['Han','Hong','Park','kim','Lee'] })
print(df1)

df2 = pd.DataFrame( {"customtmp":[1234,5678,1111,7777,3333] , 'consume':[3000,5000,6000,7000,2000] })
print(df2)

# 특정 키 기준으로 두 데이터프레임을 병합할때 사용하는  메서드 ==> merge()
# 기본  기능은 ==> 두 데이터프레임의 병합할 기준 키 데이터 중 둘다 있는 키 데이터 만 병합 ( inner )
# how = 'outer' ==> 합집합 개념으로 병합
# mergedf = pd.merge(df1,df2)
# print(mergedf)

# 동일 키가 없을 경우 merge() 해야 할 때 사용
mergedf = pd.merge(df1,df2, left_on='customid', right_on='customtmp')
print(mergedf)

# 특정 데이터프레임을 병합 할때 ==> merge(), concat()

arr1 = np.array([ [1,2,3],[4,5,6] ])
print(arr1)

arr2 = np.array([ [5,6,7],[13,15,16] ])
print(arr2)

# 디폴드 axis = 0
conarr = np.concatenate([arr1,arr2], axis=1)  # 넘파이배열을 축기준으로 병합하는 메서드
print(conarr)