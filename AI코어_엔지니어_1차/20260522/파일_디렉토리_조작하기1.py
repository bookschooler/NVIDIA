

# python_basic 디렉토리 아래에 'reference' 디렉토리를 만드시고

# '20260521' 디렉토리 내부에 존재하는 Health_info.csv 파일을
# 'reference' 디렉토리 내부로 이동
import os
print(os.getcwd())

os.chdir('C:/python_project/python_basic/')

rootdir = os.getcwd() + '\\'
print(rootdir)

# not ==> True 이면 False
# False 이면 True 로

if not os.path.exists(rootdir + 'reference'):
    os.mkdir(rootdir + 'reference')

destpath = rootdir + 'reference' + '\\'
print(destpath)

srcfilepath = rootdir + '20260521' +'\Health_info.csv'
print(srcfilepath)

import shutil

shutil.copy2(srcfilepath, destpath)

import time
print(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)