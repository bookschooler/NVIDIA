import numpy as np
import pandas as pd

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

passdf = pd.read_csv("서울특별시_지하철 승하차 승객수.csv" , encoding='CP949')
print(passdf)

# 문제)
# ==> 호선_명칭  컬럼 데이터 중  숫자문자가 있는 호선_명칭 데이터만 추출해서
# 출력주세요.
# 힌트) 정규표현식을 활용(  지난주 자료 참조 )
# 힌트) 호선_명칭 컬럼데이터를  함수적용(apply)
# 힌트) 불린배열을 형성해서 불린색인 하면 원하는 추출이  됨.
import re

def dataselect(arg):
    #print(arg)
    if len( re.findall(r'[0-9]+', arg) )  > 0:  # 숫자문자가 있다
        return True
    else:
        return False

# passdf['호선_명칭'] = passdf['호선_명칭'].apply(dataselect)
# print(passdf)

subset = passdf.loc[ passdf['호선_명칭'].apply(dataselect) ,  : ]
print(subset)