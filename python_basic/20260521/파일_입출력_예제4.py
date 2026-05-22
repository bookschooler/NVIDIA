
# # ( with~as 구문을 사용 ) filetest.txt 파일을 읽어들여서
# with open('filetest.txt', 'r+') as fi:
#     str = fi.read()
# print(str)
# # 마지막 정보를 아래와 같이 출력
#
# print ( [ item.strip() for item in str.split(',') ] )
# # ['python', 'test', 'programming', 'study', 'good']

with open("setup.log", "r+") as fi:
    strdata = fi.read()

print(strdata)

def FindCharFunc(arg1, arg2):
    count = 0
    for s in arg1:
        if s == arg2:
            count += 1
    return count

res = FindCharFunc(strdata, 'R')
print('res : ', res)