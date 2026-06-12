
import re  # regluar expression , 정규표현식

strdata = "파이썬,Ai PYThon3#Programming97@성장 빅테크"

# 패턴을 이용해서 특정 문자를 검색 ==> findall()
# 패턴을 이용해서 특정 문자열을 분할 ==> split()
# 문자열 메서드로 여러개의 구분자를 활용해 분할하기에는 문제점을 가지고 있음
# 이를 해결위해 패턴을 이용해 문자을 분할해서 사용
result = re.split(r'[,\s#@]' , strdata)
print(result)

# print(strdata)
# print(strdata.replace('#','').replace('@',''))

result = re.sub( r'[,#@\s]', ',', strdata) # 문자열 replace('k', '') 동작 유사
print(result)
# UTF-8 / CP949
with open("redata.csv", 'w', encoding="UTF-8") as fi:
    fi.write(result)  # 위 문자열 내용을 텍스트 파일로 저장!!