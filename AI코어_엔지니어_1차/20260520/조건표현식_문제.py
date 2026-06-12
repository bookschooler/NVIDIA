

srcstring = "PYTHON PROGRAMMING"

#result = srcstring.lower()  # 메서드 금지
# 리스트 내포와 조건표현식을 활용해서 구현
# 'A' ==> 65
# 'P' ==> 80
# ord() ==> 문자데이터의 원 수치 데이터를 반환하는 함수
# 원 수치 데이터를 문자데이터 형태로 변환해서 반환하는 함수  ==> chr()
listdata = [  chr( ord(s)+32 )  if s != ' ' else s for s in srcstring ]
print(listdata)
result = ''.join(listdata)
print(result)  # "python programming"

wordlist = [ "book", "car", "apple", "python", "ai" ]
# wordlist 에 문자열 항목 중 문자열의 길이가 4이상인 문자열만  새 리스트에 저장 출력
newlist = [ word for word in wordlist if len(word) >= 4 ]  # 필터링(여과기) 구문
print(newlist)

# 동일한 명령을 반복 수행할 경우 사용하는 구문 ==> 반복구문( loop 구문 )
# for(), while()
for x in [4,5,6]:
    print(x)

# 문제1) for 와  range() 를 활용해서  1 ~ 100 까지 정수의 합을 계산 출력
total = 0
for x in range(1,101):
    total += x  # total = total + x
print(total)

# 문제2)  "Python Programming,Ai Agent Programming" 이 문자열 중 'g' 문자의
#         개수를 for 반복문 활용해서 계산해서 출력
strdata = "Python Programming,Ai Agent Programming"
cnt = 0
for s in strdata:
    if s == 'g':  # s 변수의 값이 'g' 문자일 때만 조건이 참이 되서 수행
        cnt += 1
print('cnt : ', cnt)

# 문제3)  표현할 구구단의 단수를 입력 받고 해당 구구단의 내용을 출력 ( for 구문 활용 )
#         예)   출력할 구구단 단수 입력 :  7
#                 7 * 1 = 7
#                 7 * 2 = 14
#                 ...
#                 7 * 9 = 63

# dan  = int( input("표현할 구구단의 단수를 입력 : ") )
# for num in range(1,10):
#     print("{} * {} = {}".format(dan, num, dan*num))
#
# listdata = [ '짝' if '3' in str(x) or '6' in str(x) or '9' in str(x) else x for x in range(1,101)]
# print(listdata)
#
#

srcdict = {'a':1, 'b':2, 'c':3 }
destdict = {}
for key in srcdict:
    #print(key, srcdict[key])
    #dkey = srcdict[key]
    dkey = srcdict.get(key)
    destdict[ dkey ] = key # 키:value 추가 하는 문법

print(destdict)
