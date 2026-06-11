# 파이선 기본 제공 ==> 정수 범위 데이터 생성하는 클래스 ==> range

print( list( range(0,10) ) )  # 0, 1, 2, 3, ... 9

for x in range(0,3):
    print("출력")

listdata = [ ]
for x in range(0, 5):
    print("출력: ", x)
    listdata.append(x)


listdata = [ x for x in  range(0, 5) if x % 2 == 0 ]  #리스트 컴프리헨션 (list comprehension)⭐

print(listdata)


listdata = [ str(x+5) for x in range(1, 11) ]   # for 앞부분이랑 완전 뒷부분엔 조건문인 if를 붙일 수도 있음⭐
print(listdata)
print(''.join(listdata))

mystr = "kbs, mbc, sbs"
mylist = [ item.strip() for item in mystr.split(',')]

mystr1 = "Python , STudy, GooD"

#Q: 리스트 FOR문 사용해서 아래 결과 도출
print(mystr1) = ['python', 'study', 'good']

mystr1 = [item.strip().lower() for item in mystr1.split(',')]