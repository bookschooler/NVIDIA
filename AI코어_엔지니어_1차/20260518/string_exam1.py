
# 문자열 객체 ==> 시퀀스 타입
# 시퀀스 타입 ==> 데이터의 순서가 있는 타입
# 문자열 객체 ==> str()
# 특정 위치를 인덱스로 접근할 수 있음 ==> index는 항상 0부터 출발!!
str1 = "python test programming"
print(str1[5])  # [idx] : 인덱싱 문법
print(str1[-1])  # -1 : 마지막 항목의 인덱스
# 슬라이싱 문법 ( 잘라내기 문법 )
print( str1[7:11] )  # [start : stop-1] 까지 잘라내라!!
print( str1[:6] ) # python 만 출력
print(str1[12:]) # 12 부터 끝까지

# 문자열 객체에 지원되는 연산 ( +, * )
str2 = "study"
print( str1 + ' ' +  str2 )  # + 연산 : 두 문자열을 합쳐줌

# 문자열 곱셈 연산
print('='*80) # 문자열을 숫자 만큼 반복해서 생성해줌

strdata = "AI Programming"
for item in strdata:
    print(item, end=' ')
print() # 개행역할

strdata3 = "AI core"  # 문자열 상수 개념
#strdata3[0] = 'D'  # 문자열 객체의 항목을 수정할 수 없음!! ( 불변객체 )
strdata4 = strdata3.replace('A','D') # 'A' 문자 'D' 문자로 변경된 새로운 문자열 생성
print(strdata3)  # DI core
print(strdata4)

if 'te' in "python":  # "python" 문자열 객체에 "py" 문자열이 있냐? 있으면 True
    print("있음")
else:
    print("없음")