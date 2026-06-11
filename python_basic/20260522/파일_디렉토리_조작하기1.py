
# python_basic 디렉토리 아래에 'reference' 디렉토리를 만들고 그 내부로
# 20260521 디렉토리 내부에 존재하는 Health_info.csv 를 이동시켜라


import os
import shutil

os.mkdir('C:/python_project/python_basic/reference')
# shutil.move('C:/python_project/python_basic/20260521/Health_info.csv',
#         'C:/python_project/reference')
rootdir = 'C:/python_project/python_basic/'

print(os.listdir('C:/python_project/reference'))
rootdir = 'C:/python_project/python_basic'

destpath = rootdir + 'reference' + '//'
print(destpath)

srcfilepath = rootdir , '20250521' , '/Health_info.csv'
print(srcfilepath)

import shutil

shutil.copy2(srcfilepath, destpath)

import time
print(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)







