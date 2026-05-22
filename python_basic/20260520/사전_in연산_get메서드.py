
dictdata = { 'Kor':90, 'Eng':70, 'Math':80 }

print( "ps" in "python" ) # 문자열객체의 in연산

if 'Music' in dictdata: # 사전의 in 연산은 해당 사전에 키가 있냐? 없냐?
    print(dictdata['Kor'])
else:
    print("키 없음!!")

while True:
    inputdata = input("출력하고자 하는 과목을 입력 : ")
    if dictdata.get(inputdata,None):  # 키가 있으면 해당 키에 대한 value를 반환, 없으면 뒤에 명시한 값을 반환
        print(dictdata[inputdata])
    else:
        print("출력하고자 하는 과목이 없음!")