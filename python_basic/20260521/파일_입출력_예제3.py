
# 파일 입출력 ==> with as 구문
with open("pythondata.txt", "r+") as fi:
    # 파일 접근 코드만 동작
    str = fi.readlines()  # 전체 문자열 읽기

# with ~ as 구문을 벗어나는 순간 자동 close()
print(str)
#
strlist  = [ item.strip() for item in str ]  # 리스트 내포를 이용해서 리스트 항목 정리
print(strlist)