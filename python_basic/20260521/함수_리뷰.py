
# 코드의 사이즈가 커지고 큰 프로젝트를 수행해야 할 경우
# 기능 단위로 코드를 분할해서 프로젝트를 완성해야 할 경우 필수 적으로
# 기능 단위를 함수화 시켜서 사용해야한다!!
# 함수 ==> 라이브러리함수(print, input),  사용자정의함수( 직접구현 )
# 함수동작 ==> 함수정의,  함수호출
# 함수호출 ---> 함수정의 부분으로 점프해서 함수정의가 동작하고
# 함수정의에 있는 명령이 모두 종료되면 호출쪽으로 다시 되돌아 온다!!

# 함수정의 ==> def 키워드 사용
# def 함수명(매개변수):
#     #해당 함수가 동작하는 명령들의 집합을 구현
#     # ==> 함수의 기능을 서술
#     pass

# ==> 함수의 기능 : 전달인자로 넘겨온 값을 5 를 더해 그 값을 반환해줘
def AddDataFunc(arg):  # 함수 정의
    #print('result : ', arg+5 )
    # 함수의 반환값이 없을 경우 None 객체를 반환!!
    #return arg+5

    # arg 매개변수가 참조하고 있는 리스트 모든 항목 총합을 계산하고
    # 총합 과 평균을 반환
    total = 0
    for item in arg:
        total += item
    avg = total / len(arg)
    return total, avg  # return ==> 값의 반환과 함수 종료 두가지 기능을 수행

# data = 10, 20, 30
# a, b, c = ( 3, 4, 5)

# 함수호출 ==> 함수명( 전달인자 ) , 전달인자 ==> 함수정의 부분으로 던져주는 값
# res = AddDataFunc( [5,6,7,8,9] )
# print('res : ', res , type(res) )

res_total, res_avg = AddDataFunc( [5,6,7,8,9] )
print("res_tal :", res_total , " , ", "res_avg : ", res_avg)