import re

strdata = "파이썬 Ai PYThon3#Programming97@성장 빅테크"

# 패턴을 이용해서 특정 문자를 검색 == > findall()
# 패턴을 이용해서 특정 문자열을 분할 ==> split()

#   strdata.split(',').split('. ') => 이렇게 하고 싶지만 한번 split하면 문자열이
#   리스트가 되기 때문에 split을 연이어서 못씀 ==> re 패턴을 이용!!!

result = re.split(r'[,\s#@]', strdata)
print(result)

result = re.sub(r'[,#@\s]', '', strdata) # 문자열 replace('k', 'c') 동작과 유사
print(result)

with open("redata.csv", "w", encoding="cp949") as f:
    f.write(result)