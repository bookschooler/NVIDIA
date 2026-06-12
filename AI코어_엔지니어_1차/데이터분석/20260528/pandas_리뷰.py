import numpy as np
import pandas as pd

# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60,75], 'Kim':[85,95,65,55,75], 'Park':[88, 93, 75, 72,75], 'Lee':[55,66,77,92,75] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music','sci'])
print(scoredf)
scoredf.rename( index={'music':'음악'} , inplace=True)
print(scoredf)
scoredf.rename(columns={'Park':"신"} , inplace=True)
print(scoredf)

sortdf = scoredf[ ['Hong','Kim','Lee','신'] ].copy()
print(sortdf)
print("="*80)
print( scoredf.iloc[ 1:2, :]  )
# fancy index ==> 추출하고자 하는 idex의 배열을 전달
print( scoredf.iloc[ [1,3], : ] )


# timedf = pd.DataFrame( np.arange(1,51) , index= pd.date_range('2026.12.28',periods=50,freq='D') ,
#               columns=['data'] )
# # date_index = pd.date_range('2026.12.28',periods=50,freq='D')
# # print(date_index)
# print(timedf)
# timedf.info()
# print( timedf.loc['2026-12-28':'2026-12-31', : ] )
# print( timedf.loc['2026/12'])

# 문자열 타입을 ===> datetime 타입으로 변환해서 사용 ( pd.to_datetime() )
