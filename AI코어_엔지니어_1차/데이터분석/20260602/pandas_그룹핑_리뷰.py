
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현

# 엑셀파일을 전처리 해서 시각화
# index_col = 0 : 0번째 컬럼을 인덱스로 설정해서 읽어드림
youdf = pd.read_excel("youtube_data.xlsx", index_col=0) # DF 생성
import re
# 단) 함수적용 --> lambda 함수로 구현
youdf['Subscriber'] = youdf['Subscriber'].apply(lambda x : int(re.sub(r'만','0000',x)) )
#youdf['Subscriber'] = youdf['Subscriber'].apply(lambda x : int( x.replace('만','0000') ) )
#youdf['Subscriber'] = youdf['Subscriber'].str.replace('만','0000').astype('int64')
# print(youdf)
youdf.info() # 결측치 체크, 각 컬럼별 Datatype 체크
print(youdf.head(5))
pvdf = youdf.pivot_table(index='Category', values='Subscriber', aggfunc='mean')
print(pvdf)
print('='*80)
# 위 결과물이 동일하도록 groupby연산을 활용해 표현
grpdf = youdf.groupby('Category')[['Subscriber']].mean()
print(grpdf)
#print(pvdf.values,  type(pvdf.values))

grpdf.sort_values(by='Subscriber', ascending=False, inplace=True)
grpdf_top7 = grpdf.head(7).copy()
print(grpdf_top7)