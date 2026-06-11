
# 시퀀스 타입 ==> 문자열, 리스트, 튜플

listdata = [ [5,6], "python", 5.9 ] # == list()  이 명령과 동일
print( listdata[1] )  # read
listdata[1] = "AI" # write

tupledata = (50,"python") # == tuple() , 읽기 전용

import numpy as np

# arr1 = np.array( [ [3,4,5,6,7],[7,8,9,2,1]  ] )
# print(arr1)
# print(arr1.ndim) # 차원수
# print(arr1.shape)  # 형태 ==> tuple 형태로 반환

arr1 =  np.arange(1,10).reshape( (3,3) )
print(arr1)
print(arr1.shape)

d1, d2 = (3,5) # 튜플의 unpack

a = 5
b = 7
print(a,b) # 5, 7

a, b = b, a

print(a,b) # 7, 5

# 매핑 타입 ( 사전 )
dictdata = { 'A': 50, 'B': 90 } # == dict() ,  매핑 타입 (  키 : 값 )
dictdata['C'] = 70  # 기존 키가 없으면 키 와 값을 새로 추가
dictdata['B'] = 33  # 기존의 키가 존재하면 value 를 업데이트

print(dictdata)
print(dictdata['A'])
for key in dictdata:  # 반복문에 사전이 오면 키가 반환되서 전달!!
    print(key, dictdata[key])

# set 타입 ( 집합타입 ) ==> 수학의 집합연산( 합, 교, 차, 여 )을 지원
data1 = {50, 90, 60, 70} # ==set()
print(data1, type(data1))
# 셋타입은 중복데이터를 허용하지 않음!!
listdata = [5, 1, 8, 8, 7, 3, 1, 5]
print(set(listdata))
data2 = {90, 60, 80, 30}
print(data1 - data2)  # 차집합연산
print(data1 | data2)  # 합집합연산
print(data1 & data2)  # 교집합연산
print(data1 ^ data2)  # 여집합연산
#
# import random  # 파이썬 기본제공
#
# # 임의의 정수를 추출해서 사용 ==> 기본 제공 randint()는 하나의 정수를 반환하는 제약
# result = random.randint(10,20)  # 10 ~ 20 사이에 있는 임의의 정수 하나를 반환해줘!!
# print(result)
#
# result = np.random.randint(1,46,(5,6))
# print(result)