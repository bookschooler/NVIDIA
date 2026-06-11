# print() ==> 문자열을 출력하는 함수
# input() ==> 키보드로 문자열을 입력하는 함수

data1 = input("데이터 입력: ")   # " " 문자열을 화면에 출력하고 입력 대기 상태
data2 = input("데이터 입력: ")
print(data1 + data2)

# 문자열 객체 ==> 정수 객체로 변환: 타입 변환(CAST)


# 문자열 비교 예

saved_pw = 'python'

while True:
    input_str = input("password 입력 (종료: quit) ==>  ")
    if input_str == saved_pw:
        print('pw success!!')
    elif input_str == 'quit':
        break
    else:
        print('pw fail!!!')


