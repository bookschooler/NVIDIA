
# # print() ==> 문자열 출력
# # input() ==> 키보드로 부터 문자열을 입력하는 함수
# # ==> 입력받은 데이터를 문자열객체 처리 함!!
# data1 = int( input("정수 데이터 입력 : ") ) # "  " 문자열을 화면에 출력하고 입력 대기 상태
# data2 = int( input("정수 데이터 입력 : ") )
#
# # 문자열 객체 ==> 정수 객체로 변환 : 타입 변환(cast)  ,
# print(data1 + data2)
#
# print( int("1234") + int("5678") )

pw_str = "python"

while True:
    pasword = input("패스워드 입력(quit) : ")
    if pasword == pw_str:
        print("패스워드 입력 성공!!")
    elif pasword == 'quit':
        break  # 반복문 탈출
    else:
        print("패스워드 입력 실패")