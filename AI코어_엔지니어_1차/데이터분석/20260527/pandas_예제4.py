import numpy as np
import pandas as pd

# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60,75], 'Kim':[85,95,65,55,75], 'Park':[88, 93, 75, 72,75], 'Lee':[55,66,77,92,75] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music','sci'])
print(scoredf)
# Kim 사람의 기준으로 70 점 이상인 행 데이터만 추출 및 출력

print( scoredf['Kim'] >= 70 )  # 불린 배열 ( Boolean 배열 )

# 불린배열을 색인 인덱스로  사용해서 추출 ==> 불린색인은 loc만 지원
# 불린 배열의  True 항목만 자동 추출
subset = scoredf.loc[   scoredf['Kim'] >= 70  , 'Kim' : 'Park'  ].copy()
print(subset)

print("="*80)
print(scoredf)
# 특정 컬럼 데이터 선택
print(scoredf[['Hong','Park']])  # 여러 컬럼 선택