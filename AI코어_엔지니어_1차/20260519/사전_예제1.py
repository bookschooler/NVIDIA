
# 시퀀스 ==> 문자열 "", 리스트 [], 튜플 ( )

# 매핑 타입 ==> 사전타입 ==> dict 클래스

data1 = { } # == dict() , 빈 사전 객체 생성 ,  키 : value 으로 매핑 상태
print(data1, type(data1))
# 키는 변경할수 없는 객체가 와야함!!
# 사전에  항목을 추가
data1[ "AB" ] = 90
data1['DF'] = 30
print(data1)

# 사전에 value 읽기
print( data1["DF"] ) # 키를 주면 해당 키에 대한 value 를 반환

data1['New'] = 50
print(data1)

# 항목 추가시 기존 키가 있으면 해당 키에 대한  value를 업데이트
data1['DF'] = 700
print(data1)

# 항목 삭제
del data1['DF']
print(data1)

scoredict = { 'kor':90, 'eng':80, 'math':70 }
total = 0
for key in scoredict:  # 반복문에 사전이 올 경우 변수에는 키가 전달되면서 반복
    print(key, ' : ', scoredict[key])
    total += scoredict[key]  # total = total + scoredict[key]

print('total : ', total)