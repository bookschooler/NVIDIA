# 텍스트 파일 (.txt)은 파일 입출력 코드로 접근하는 게 편함.
# 파일 개방 함수 ==> open(), 접근할 파일의 경로 + 파일명, 접근모드를 설정
# 접근모드 ==> 'r' (읽기), 'w' (쓰기), 'a' (추가), 'r+' (읽기/쓰기) 가능모드
# 파일 해제함수 ==> close()
# with ~ as 구문을 활용 / with ~ as 구문을 벗어나면 자동으로 close 되게 해줌
with open("C:/python_project/python_basic/20260521/pythondata.txt", 'r+') as fi:
    # str = fi.read()     # 전체 문자열
    # str = fi.readline()     # 한 줄씩 반환
    str = fi.readlines()    # 리스트로 반환

print(str)

listdata = [ x.strip() for x in str]
print(listdata)

import pandas as pd
mydf = pd.DataFrame(listdata)
print(mydf)
mydf.to_excel('pythondata.xlsx', index=False)




# import os
# print(os.getcwd())
# print(os.listdir("C:/python_project/python_basic/20260521)") # 리스트 안 주면 현재 경로를 반환함.