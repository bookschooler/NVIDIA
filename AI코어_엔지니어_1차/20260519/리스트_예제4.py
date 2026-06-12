

# 파이썬 기본 제공 ==> 정수 범위데이터 생성하는 클래스 ==> range

print( list( range(0,10) ) )  # 0, 1, 2, 3, ...9

# listdata = []
# for x in range(0,5):
#     print("출력 : ", x)
#     listdata.append(x)

listdata = [ x for x in range(1,11) if x%2 == 0 ]  #  리스트 내포 + 여과 문법

print(listdata)

listdata = [ x+5 for x in range(1,11) ]  #  리스트 내포 + 여과 문법
print(listdata)
#print(''.join(listdata))

mystr = "kbs , mbc , sbs"
#print( mystr.split(',') )
#mystr = ['kbs ',' mbc ', ' sbs']
mylist = [ item.strip() for item in mystr.split(',')]
print(mylist)

mystr1 = "Python , STudy, GooD"

# 리스트 내포 구문을 활용해서 아래 결과를 도출
mystr1 = [ item.strip().lower() for item in mystr1.split(',')]
print(mystr1)  # ['python', 'study', 'good']


mylistdata = ["python","prog","good"]

for idx, item in enumerate(mylistdata):
    print(idx,' : ', item)