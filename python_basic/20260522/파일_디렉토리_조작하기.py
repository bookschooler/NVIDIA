import os
import sys  # 이게 os보다 한 단계 상위 레벨, 건드릴 때 조심할 것!
import shutil   # shell util 쉘 유틸리티

print( os.getcwd() )
rootdir = os.getcwd() + "\\"
print(rootdir)

# os.mkdir(rootdir + '\dataset')
# print(os.listdir())     # 현재 작업 디렉토리내에 모든 파일 및 디렉토리 정보를 출력
#
# if os.path.exists(rootdir + '\dataset'):
#     shutil.move(rootdir + '\pythondata.txt', rootdir + '\dataset')

# os.rmdir(rootdir + 'dataset') # 디렉토리 내부에 파일이 하나라도 존재하면 삭제 안 됨.
shutil.rmtree(rootdir + 'dataset')
