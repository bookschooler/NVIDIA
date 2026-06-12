import numpy as np
import pandas as pd

# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60], 'Kim':[85,95,65,55], 'Park':[88, 93, 75, 72], 'Lee':[55,66,77,92] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music'])
print(scoredf)
#  문제
# kim, park 의 eng 와 math 정보만 추출 및 출력
# 하나는 loc 사용,  하나는 iloc 사용 해서 두번 출력
# scoredf.loc[ 행인덱스, 열인덱스 ] ==> 한 위치 데이터만 접근
# scoredf.loc[ 행슬라이싱, 열슬라이싱 ]  ==> 여러개의 범위 데이터 접근
# label(문자열) 인덱스는 마지막 stop 을 포함
# 수치(정수) 인덱스는 stop-1 까지 포함
# subset = scoredf.loc[ 'eng': 'math' , 'Kim': 'Park' ].copy()
# print(subset)
# # subset DF 에서 Park 의 eng 점수를 99로 수정
# subset.loc['eng','Park'] = 99
# print(subset)
# print(scoredf)

subset = scoredf.iloc[ 1:3, 1:3].copy()
print(subset)
subset.iloc[0,1] = 99
print(subset)
print(scoredf)

# scoredf['subject_total'] = [ scoredf.loc['kor'].sum(), scoredf.loc['eng'].sum(), scoredf.loc['math'].sum() ]
# #print ( [ int( scoredf.loc[idx].sum() ) for idx in scoredf.index] )
# print(scoredf)
# print(scoredf.columns)
# print(scoredf['Hong'].mean())
#
# scoredf.loc['sub_mean'] = [ scoredf[col].mean() for col in scoredf.columns ]
# print(scoredf)