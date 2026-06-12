
max = 0
# max 변수에는 두 변수의 큰 값을 체크해서 저장
data1 = 150
data2 = 90
# if data1 > data2:
#     max = data1
# else:
#     max = data2
# 간단한 if~else 구문을 한 라인으로 표현한 구문 ==> 조건표현식 구문
max = data1 if data1 > data2 else data2
print("max : ", max)

# 조건표현식 과 리스트내포 구문을 하나로 표현해서 사용
listdata = [ "짝" if x%2==0 else "홀" for x in range(1,10) ]
print(listdata)

