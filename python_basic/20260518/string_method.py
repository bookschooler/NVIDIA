name = "신순록"
age = 29

print("나의 정보 ==> 이름:{} , 나이 : {}".format(name, age))
print(f"나의 정보 ==> 이름:{name} , 나이 : {age}")

strdata = "python programming"
print(strdata.capitalize()) # p-> P 로 바뀐 새로운 문자열 객체가 생성된 상태임!   #⭐

strdata1 = """python programming    #⭐
test python prog
python bad
"""

print(strdata1.count('python'))

strdata2 = "test programming"
newstring = (strdata2.replace(" ", "_")) #⭐

strdata3 = newstring.split("_") #문자열 객체를 특정 문자기준으로 분할해라!⭐
print(strdata3) #결과를 리스트로 반환!
print(strdata3[1])

string_exam = "kbs ,  mbc, jtbc , sbs"

print(string_exam.replace(" ", ""))
new_string = string_exam.split(',')
print(new_string)

listdata = []
for i in new_string:
    listdata.append(i.strip())
print(listdata)


listdata = [ item.strip() for item in new_string ] #⭐고급 버전
print(listdata)

listdata1 = [ 'kbs', 'jtbc', 'mbc', 'sbs']
newdata = ",".join(listdata1)   #⭐
print(newdata)

listdata4 = "python#test ai programming, study"
ref1 = listdata4.replace('#', ' ').replace(',', '').split(' ')
print(ref1)

# 정규표현식
import re
listdata4 = "python#test ai programming, study"
result = re.sub(r'[#,]',' ',listdata4)  #⭐정규표현 복습!
print(result)

list_exam = []
print(list_exam, type(list_exam))
list_exam.append()
list_exam.extend()

data = { }  # 딕셔너리 객체 생성
data1 = ( )  # 튜플 객체 생성

