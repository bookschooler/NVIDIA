

# 0 ~ 전달해주는 특정 정수까지의 총합을 계산하는 함수
# arg=10  ==> 기본값을 갖는 매개변수(파라미터) 설정 ( 디폴트파라미터 )
def SumofintData(data, arg=10):   # 함수 정의
    total = 0
    for x in range(arg):
        total += x

    print("total : ", total)

SumofintData(50, 7)  # 함수 호출




# 전달인자가 여러개 일 경우 처리하는 함수
# *arg  ===> 여러개의 전달인자를 하나로 묶어서 받곗다!! ( tuple 처리 )
def SumofData( argdata, *arg):
    print(argdata)
    print(arg , type(arg))


SumofData( 3, 5, 6, 7, 8, 9 )  # 함수호출



# dict 형태 처리 함수
def MyDictFunc( **arg ):
    print(arg , type(arg))


MyDictFunc( a = 100,  b  = 30,  c = 90)


def MyDataControl( arg ):
    print(arg)
    total = 0
    for item in arg:
        print( item[1] )
        total += item[1]
    return total


datalist = [ (3,4), (5,6), (7,5) ]
result = MyDataControl(datalist)
print('result : ', result)  # 15

