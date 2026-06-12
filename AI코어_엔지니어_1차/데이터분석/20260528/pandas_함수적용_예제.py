import numpy as np
import pandas as pd

arr = np.arange(1,10).reshape(3,3)
print(arr)
print( arr.mean(axis=0) )  # 제공해주는 집계(통계) ==> sum, min, max, mean

mydf = pd.DataFrame(arr , columns=['a','b','c'] )
print(mydf)
print(mydf['a'].mean(), mydf['a'].max())


def MyAddFuc(arg):
    return arg+5

#result = MyAddFuc(7)
#f = lambda x : x+5  # 이름이 없는 함수 ==> lambda 함수(객체)
result = (lambda x : x+5)(7)
print(result)

print( np.power(5,3) )  # ==> 제곱승 연산
print( 5**3 )


# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60,75], 'Kim':[85,95,65,55,75], 'Park':[88, 93, 75, 72,75], 'Lee':[55,66,77,92,75] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music','sci'])
print(scoredf)

scoredf['성별'] = ['male', 'female', 'female','male','female']
print(scoredf)
scoredf.info()
# Dataframe 또는 Series 의 각 요소에 특정 함수를 일괄 적용시켜서
# 동작하는 기능을 함수 적용 ==> map(), apply()

# def DataControl(arg):
#     print('arg : ', arg)
#     if arg == 'male':
#         return 1
#     elif arg == 'female':
#         return 0
#

scoredf['성별'] = scoredf['성별'].map( {'male':0,'female':1} )
print(scoredf)

def ScoreIncrese(arg):
    return arg+5

scoredf['Hong'] = scoredf['Hong'].apply(ScoreIncrese)
print(scoredf)
#print( scoredf['Hong'].apply(lambda x : x+5) )
