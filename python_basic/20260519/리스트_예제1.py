# 리스트 ==> 시퀀스 타입 객체

# = (대입연산) ==> 왼쪽의 내용을 오른쪽으로 복사 대입하는 역할
# == (비교 연산) ==> '같음'을 나타내는 기호
# ===> 비교 연산의 결과물은 항상 ==> True or False 만 나옴

list() # 리스트 타입의 객체 생성

# 리스트는 문자열과 달리 항목을 Read / Write가 가능
data1 = [80, 90]  # == list() 이 때는 아직 id고 뭐고 메모리에 안잡힌 상태, 그래서 인덱스로 값을 할당할 수 없음.
print(data1, type(data1))
data1[0] = 50   # 항목 수정
print(data1)    #[ 50 ]

data2 = []
# 빈 리스트 객체에 내용물을 추가하는 코드
# 리스트에 내용물을 추가하는 메소드(함수) ==> append(), extend(), insert()
# append 하나의 객체만 추가, extend는 넣는 거 하나하나 풀어서 추가, insert는 위치 지정해서 추가

data2.append(60)
data2.append("python")
data2.append(5.8)
data2.append(["programming", [90,'nvi']])
print(data2)

# 리스트는 항목으로 오는 객체의 타입에 제한이 없음 => 어떤 객체 타입이든 항목으로 올 수 있음.

# 문제: 'v'하나만 나오게 하려면?
print(data2[3][1][1][1])