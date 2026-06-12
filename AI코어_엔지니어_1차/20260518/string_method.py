

name = "홍길동"
age = 50

print("나의 정보 ==> 이름 : {} , 나이 : {}".format(name,age))
print(f"나의 정보 ==> 이름 : {name} , 나이 : {age}")

strdata = """python programming
test python prog
python good
"""
print( strdata ) # p -> P 로 바뀐 새로운 문자열 객체가 생성
print(strdata.count('python'))

strdata1 = "test python programming"
newstring = strdata1.replace(" ",",")
print(newstring)
result = newstring.split(',') # 문자열 객체를 특정 문자기준으로 분할해라!!
print(result)  # 결과를 리스트로 반환
print()
print(result[2])

string_exam = "kbs , mbc, jtbc ,sbs "
newstring = string_exam.split(',')
print(newstring)
# listdata = []
# for item in newstring:  # 시퀀스 객체의 반복문은 항목이 하나씩 변수에 전달되면서 수행
#     #print(item.strip())
#     listdata.append( item.strip() )
# print(listdata)
listdata = [ item.strip() for item in newstring]
print(listdata)
# print(newstring[0].strip())
# print(newstring[1].strip()) # strip() : 앞뒤 공백 , 개행 모두 제거
# print(newstring[2].strip())
# print(newstring[3].strip())


listdata1 = ['kbs', 'mbc', 'jtbc', 'sbs']

newdata = ",".join(listdata1)
print(newdata)

import re    #   정규표현식
listdata3 = "python#test ai programming,study@good"
result = re.sub(r'[#,@]',' ',listdata3)
print(result)

# result = listdata3.replace('#',' ').replace(',',' ')
# print(result)

listdata4 = ['test', '30', 'good']
print( ' '.join(listdata4) )

list_exam = [] # == list()  # 클래스명() ==> 객체생성
data = {} # == dict() # dict 클래스를 이용해서 객체 생성
data2 = () # == tuple()

print( list("abcdef") )