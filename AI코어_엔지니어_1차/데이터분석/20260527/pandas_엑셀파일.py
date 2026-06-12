import numpy as np
import pandas as pd

popdf = pd.read_excel("population_in_seoul.xls") # 엑셀파일 읽어서 DataFrame 객체로 생성
#print(popdf)
# 특정 파일을 읽어서 Dataframe 객체로 생성했을 경우 항상
# Dataframe 객체의 정보를 확인 ==> info()
popdf.info()
# print( popdf.head() )  # 첫행부터 ~~ 5행까지 선택해서 추출
# print( popdf.tail() )   # 마지막부터 위로 5행 선택 추출
# print( popdf.sample(n=5) )  # 랜덤으로 5행  추출
#
print(popdf)

print("="*80)
# 행으로는 '합계' 가 있는 행 삭제
popdf.drop([0],axis=0, inplace=True)
# 열로는 '고령자' 컬럼 열 삭제
popdf.drop(['고령자'], axis=1, inplace=True)
print(popdf)


# 결측치 검사
#print( popdf['남자'].isnull()  ) # innull(): 항목이 NaN 이면 True, NaN 아니면 False
#  불린 배열을 형성
# print(  popdf.loc[ popdf['남자'].isnull() , : ] )
# print(  popdf.loc[ popdf['여자'].isnull() , : ] )
for col in popdf.columns:
    print(popdf.loc[popdf[col].isnull(), :])
    print("컬럼 : ", col)
    print("="*80)

# NaN 하나라도 있는  행을 삭제
# popdf.drop([2,6,8,15],axis=0, inplace=True)
# print(popdf)

# 결측치가 있는 행을 찾아서 삭제하는 메서드 ==> dropna()
# how = 'any' ( 행에 하나도 결측치가 있으면 삭제 ), how = 'all' ( 행에 모든 데이터가 NaN일때 삭제 )
popdf.dropna(axis=0,how='any', inplace=True)
print(popdf)

# 결측치를 삭제하고 난 이후에는 항상 인덱스를 초기화
# 인덱스를 초기화 메서드 ==> reset_index()
popdf.reset_index(drop=True, inplace=True) # 디폴트 기능 ==> 기존 인덱스를 컬럼열로 올리고 인덱스를 초기화
# 컬럼열로 올리지 말고 그냥 기존 인덱스 삭제해.(버려) ==> drop = True
print(popdf)

# 특정 컬럼 데이터를  인덱스로 설정해서 사용!!  ==> set_index()
popdf.set_index('자치구', inplace=True)
print(popdf)

#  남자 컬럼 기준으로 인구수 20만 이상인 데이터만 추출해서
#  막대 그래프로 시각화 하세요!!






