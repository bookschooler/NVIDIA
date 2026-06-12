
# 리스트 ==> 시퀀스 타입 객체 ( 색인연산, 슬라이싱 연산, +, *  )
# = ( 대입연산 ) ==> 왼쪽에 내용을 오른쪽으로 복사 대입하는 역할
# == ( 같냐? ) ==> 관계(비교) 연산 ==> a > b , a < b , >= , <=, != , a == b
# ==> 비교연산의 결과물은 항상 ==> True, False 만 나옴

# 리스트는 문자열과 달리 항목을 R/W 가능한 객체다!!
data1 = [80,90] # == list() # 빈 리스트 타입의 객체 생성
print(data1, type(data1))  # [80, 90]
data1[0] = 50  # 항목 수정 (쓰기)
print(data1[1]) # 리스트 객체 내용을 리드(읽기)

data2 = []
# 빈리스트 객체에 내용물을 추가 하는 코드
# 리스트에 내용물 추가하는 메서드(함수) ==> append(), extend(), insert()
# object ==> 하나의 객체를 전달
data2.append(60)
print(data2)
data2.append("python")
print(data2)
data2.append(5.8)
print(data2)
# 리스트는 항목으로 오는 객체에 제한이 없다!! ( 즉, 어떤 객체든지 항목으로 올수 있다!! )
data2.append(["programming", [90,'nvi']])
print(data2)
# 문제
print(data2[3][1][1][1])  # 'v' 문자 하나만 출력
print('='*80)
# iterable ==> 시퀀스객체를 의미
data2.extend([50,90,70])  # 여러개의 객체를 동시에 추가 할때 사용!!
print(data2)
print('='*80)
data2.insert(2,30)  # 특정 위치에 항목을 추가는 메서드
print(data2)

# 항목 삭제
print(len(data2))  # len() : 항목의 길이 계산 ( 개수 )
print(data2)
# del 키워드를 활용해서 삭제
del data2[4]
print(data2)