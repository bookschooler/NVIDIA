import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns  # 시각화 패키지(라이브러리)
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

youdf = pd.read_excel("youtube_data.xlsx", index_col=0) # 엑셀파일 읽어서 DataFrame 객체로 생성
#print(youdf)
#youdf.info()
print( youdf.head(30) )
# 데이터중에 Category 가 가장 많은것이 뭡니까?

data =  youdf['Category'].value_counts() # Series
# Series ==> Dataframe 객체로 변환
datadf = pd.DataFrame(data)
print(datadf)
datadf.index.name = ''
print(datadf)
# count 컬럼명을 카테고리개수 로 수정
datadf.rename( columns={'count':"카테고리개수"} , inplace=True)
print(datadf)

datadf_top5 = datadf.head(5).copy()
print(datadf_top5)

plt.pie(x=datadf_top5['카테고리개수'], labels=datadf_top5.index,
        autopct="%.2f%%")  # 파이차트 랜더링 함수

plt.show()