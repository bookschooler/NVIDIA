# 데이터에 순서가 있는 타입 : 시퀀스 타입
# 문자열 객체는 str() 를 사용해서 만듦
# 근데 동적 타이핑 가능해서 " " 이나 ' ' 하면 자동으로 만들어짊
# 시퀀스 타입은 인덱스로 접근할 수 있음

str1 = "It is my first day"
print(str1[5])   # [idx] 인덱싱 문법
print(str1[-1])  # 마지막 항목의 인덱스

# 슬라이싱 문법(잘라내기)
print( str1[7:11])  # [start: stop-1]까지 잘라내라!
print( str1[:6])    # python 만 출력
print( str1[12:])   # 12부터 끝까지

# 문자열 객체에 지원되는 연산(+, *)
str2 = "Let's go home now"
print(str1 + ' ' + str2)  # +연산: 두 문자열을 합쳐줌

# 문자열 곱셈 연산
print('='*80)

strdata = "AI Programming"

for i in strdata:
    print(' '.join(i))

for i in strdata:
    print(i, end=' ')
print() # print() 안에 아무것도 안쓰면 이것도 줄 바꿈할 때 씀!
print('\n') #이건 두 줄 띄우겠다는 뜻

strdata3 = "AI core"
# strdata3[0] = "D"   #한번 생성된 문자열 객체의 항목을 수정할 수는 없.음!!! => 그래서 불변객체라고 함!
print(strdata3) #DI core

strdata4 = strdata3.replace('A','D')
print(strdata4)


if 'py' in "python": #"python" 문자열 객체에 'py' 문자열이 있나?  있으면=> True , 없으면=> False
    print("있음")


