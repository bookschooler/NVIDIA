import numpy as np  # as : numpy 를 np로 사용하겠다 라는 별칭 부여 문법

# 1, 2, 3, 다차원 배열 형태의 데이터를 생성하고 연산할 필요
# 넘파일 배열을 생성
# arr1 = np.array(  [ [ [5],[6],[7],[8] ] , [ [5],[6],[7],[8] ] ] )  # 리스트를 이용해서 넘파일 배열 객체를 생성
# print(arr1)
# print( arr1.ndim ) # 배열의 차원수 반환
# print( arr1.shape ) # 배열의 형태를 튜플로 반환

# 범위데이터를 이용해서 넘파일 배열을 생성
arr2 = np.arange(1,21).reshape( (4,5) )
print(arr2)
# 넘파이 배열 select 문법
print( arr2[1][2] )
print( arr2[3][3])

subset = arr2[1:3 , 1:3 ]  # arr2[ 행슬라이싱, 열슬라이싱 ]
print(subset)

subset = arr2[1: , 3: ]  # arr2[ 행슬라이싱, 열슬라이싱 ]
print(subset)

subset = arr2[:3 , :3 ]  # arr2[ 행슬라이싱, 열슬라이싱 ]
print(subset)

# # 임의의 난수 넘파이 배열 생성
# arr3 = np.random.randint(1, 100, (4,5))
# print(arr3)


arr_zero = np.zeros((13,13))  # 배열을 내용을 0으로 채워서 배열을 생성해줌
print(arr_zero)

arr_zero = np.ones((13,13))  # 배열을 내용을 0으로 채워서 배열을 생성해줌
print(arr_zero)






