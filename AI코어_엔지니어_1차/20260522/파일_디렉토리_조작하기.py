import os
import shutil  # shell util

#print( os.getcwd() ) # 현재 작업 경로 출력
rootdir = os.getcwd() + "\\"
print(rootdir)
# os.mkdir(rootdir + 'dataset')
# print(os.listdir()) # 현재 작업 디렉토리내에 모든 파일 및 디렉토리 정보를 출력
#
# if os.path.exists(rootdir + 'dataset'):
#     shutil.move(rootdir + 'pythondata.xlsx', rootdir + 'dataset')

#os.rmdir(rootdir + 'dataset') # 디렉토리 내부에 파일이 하나라도 존재하면 삭제안됨
shutil.rmtree(rootdir + 'dataset')