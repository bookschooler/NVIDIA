
# 파일입출력 ==> open(), close()
# open() : 파일 개방 ==> 파일을 파일객체화
# close() : 파일객체 해제

f = open("pythondata.txt", "r+") # 'r+' : 읽고쓰기 가능 모드
strdata1 = f.read() # 텍스트파일에 작성된 모든 내용을 읽어서 문자열 객체로 생성
print(strdata1)
print( f.tell() ) # 현재 파일포인터 위치를 반환
# #strdata = f.readline()  # 텍스트파일에 첫번째 한 줄만 읽어서 문자열 객체 생성
# f.seek(0,0) # 파일포인터 맨위로 초기화
# print( f.tell() )
# strdata2 = f.readlines() # 각 라인의 텍스트를 리스트의 항목으로 넣어서 리스트로 반환
# print(strdata2)
f.write("\ntest")

f.close()  # 파일객체 메모리 해제