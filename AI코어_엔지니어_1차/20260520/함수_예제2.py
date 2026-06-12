
def listsumofdata(arg):  # 함수정의 -->  함수명(매개변수)
    print(arg)  # 기능구현 ==> arg 참조하는 리스트 항목의 총합을 계산
    total = 0
    for x in arg:
        total += x
    return total

res = listsumofdata( [60,77, 88, 33] )  # 함수호출(전달인자)  --> 함수정의로 점프
print('res : ', res) # 전달한 리스트의 총합을 출력



def addlistdata( arg1, arg2 ):  # 함수 정의
    listdata = []
    for idx, item in enumerate(arg1):
        #print(idx, item)
        #print( item + arg2[idx] )
        listdata.append( item + arg2[idx] )
    return listdata

result = addlistdata([5,6,7,8],[2,3,4,5])  # 함수호출
print('result : ', result) # [7,9,11,13]



# CheckAlphaData() : 기능 ==> 앞에 전달된 문자열 중 뒤에 전달된 문자의 개수를 파악해서 반환
def CheckAlphaData(arg1 , ch):
    print(arg1, ch)
    count = 0
    for s in arg1:
        if s == ch:
            count += 1
    return count

cnt = CheckAlphaData("python programming" , 'a')  # 함수호출
print('cnt : ', cnt)  # 2



