

def ReveseData():
    #global data, value  # 전역공간 등록된 두변수를 활용(사용)
    #data, value = value, data
    return 70, 50

data = 50
value = 70
print(data, value)  # 50  70  --> 함수 호출 전
data, value = ReveseData()  # 함수 호출
print(data, value)  # 70  50 --> 함수 호출 후
