
# 파이썬 조건문 ==> 단독 if구문,  if~else구문,  if~elif~elif~else 구문
# 조건문 ==> 프로그램의 흐름을 제어하는 역할의구문 ( 제어문 )
# 조건표현식 ==> 참, 거짓을 반환하는 문법을 사용
# 비교(관계) 연산자 ==> a > b , a < b, a <= b, a >= b, a == b,  a != b
# 비트연산자 ==> ~ , & , | , ^
# 논리연산자 ==> or (하나의 항이라도 True이면 전체가 True),
# and ( 하나의 항이라도 False 이면 전체가 Fasle )
# 사칙연산 ==> + , - , * , / , %(나머지연산)
print( ( 5 != 3 ) and ( 3 > 1) )
print ( 5 % 3 )

# 컴퓨터에서는 0 이외에 모든 숫자는 참(True)!!
data = 3
if data == 5:   # 단독 if 구문 --> if~else 구문으로 확장
    print("data는 5")   # 조건이 참일때 수행하는 구문
else:
    print("dats는 5가 아님!!")  # 조건이 거짓일때 수행하는 구문

# 조건의 경우의 수가 많을 경우 사용하는 구문 ==> if ~ elif ~ elif ~ else

while True:
    print("메뉴 : 1.사이다 2.콜라 3.생수 4.쥬스 5.프로그램종료")
    selmenu = int( input("메뉴 하나를 선택 : ") ) # 기본적으로 문자열 객체처리
    if selmenu == 1:
        print("사이다를 선택!!")
    elif selmenu == 2:
        print("콜라를 선택!!")
    elif selmenu == 3:
        print("생수를 선택!!")
    elif selmenu == 4:
        print("쥬스를 선택!!")
    elif selmenu == 5:
        print("프로그램 종료합니다!!")
        break  # 반복문 탈출 역할의 구문
    else:   # 위 조건을 하나도 만족하지 않을 경우 수행하는 구문
        print("1 ~ 4 까지 메뉴만 선택주세요!!")

