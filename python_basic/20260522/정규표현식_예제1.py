import re   # regular expression

strdata = "파이썬 Ai PYThon3 Programming97 굿 2026A+ B- C ALL In ONe !! 빅테크"
# 문자열 메소드가 아닌 특정 패턴을 활용해서 특정 문자열을 찾고(검색), 분할하고,
# 치환(삭제) 할 수 있는 정규표현식 메소드를 지원

# 검색  ==> findall() ==> 패턴에 매칭되는 모든 내용을 리스트 형태로 받음

# [ ] ==> 여러 개의 패턴을 하나루 묶어서 표현할 때 사용하는 메타문자
# + ===> + 기호 앞에 있는 패턴이 하나 이상인 걸 찾아라!
# ? ===> ? 기호 앞에 있는 패턴이 0번 또는 1번 인 걸 찾아라!
# * ===> * 기호 앞에 있는 패턴이 0번 이상인 걸 찾아라!

result = re.findall(r'[^a-zA-Z0-9가-힣]+', strdata)

# result = re.findall(r'B', strdata)
# if not result:
#     print("없어요")
# else:
#     print("있어요")
# # print(result) ==> 이러면 빈 리스트 [] 나옴. False이기 때문

# 영어 대문자만 찾아볼까?
# result = re.findall(r'[A-Z]', strdata)   # r'   => 이건 패턴이다! 라고 알려주는 거!

# 영어 소문자 패턴
# result1 = re.findall(r'[a-z]' , strdata)
# print(result1)

# # 영어 대소문자 패턴
# result1 = re.findall(r'[a-zA-Z]+' , strdata)
# print(result1)
#
# # 한글이 하나 이상인 패턴
# result1 = re.findall(r'[가-힣]+' , strdata)
# print(result1)

# # 숫자가 하나 이상인 패턴
# result1 = re.findall(r'[0-9]+' , strdata)
# print(result1)

# result1 = re.findall(r'[A-Z]+' , strdata)
# print(result1)

strdata = "Ai반 Ai Ai구축 Ai프로그램 Ai"
result = re.findall(r'Ai\w*', strdata)
print(result)



