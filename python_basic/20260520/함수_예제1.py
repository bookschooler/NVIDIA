
# 함수 ==> 코드의 유지보수 , 코드 재활용을 향상 시키는 기능
# 특정 기능을 분할해서 완성코드를 구현하는 목적
# y = f(x)
# 함수 구현 ==> 함수 정의, 함수 호출
# 함수 정의 ==> 특정 기능의 명령어 집합 ==> def 키워드로 시작
# 함수 호출 ==> 특정 함수 정의 부분으로 점프 ==> 함수명으로 시작

# def 함수명():   ==> 함수정의 ( 매개변수 )
def Comnamedisply(arg1, arg2):
    print( f"{arg1} {arg2} AI Core" )
    return arg2 + 20  # return ==> 함수의 종료와 값의 반환
    # 함수의 반환값이 없을 경우 None 객체를 반환

# 함수호출
print("프로그램 시작")
result = Comnamedisply("Hong", 80) # 함수명( 전달인자 )
print(result)

def InputData():  # 함수정의
    numdata = int( input("정수하나 입력 : ") )
    return numdata

data1 = InputData() # 함수호출
print('data1 : ', data1)
print("프로그램 종료")


