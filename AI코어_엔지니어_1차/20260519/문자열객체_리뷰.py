
# 시퀀스 객체 ==> 데이터의 순서가 있는 객체 ==> 문자열, 리스트 , 튜플
# 객체지향언어 ( OOP ) ==> 특정 클래스를 바탕으로 객체를 생성해서 프로그램이 동작
# 객체 생성 문법 ==> 클래스명()

data1 = "python"
# data1.join()
# data1.replace()
# data1.format()
# data1.split()
# data1.strip()
# data1.upper() # 대문자로 변환
data2 = '800'

data1[0]  # [idx] : 색인연산 , idx는 항상 0부터 출발
data1[2:4]  # [start : stop-1] : 슬라이싱문법

data1 + data2  # 두 문자열을 합쳐줌
data1 * 5 # 문자열을 회수만큼 반복해서 생성
print("="*80)
print( list(data1) )  # 타입변환
for item in data1:
    print(item, end=' ')