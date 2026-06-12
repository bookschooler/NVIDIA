import numpy as np
import pandas as pd

# 3.넘파이 배열을 활용한 DataFrame 객체생성
mydf = pd.DataFrame(  np.arange(10,25).reshape( (5,3)) , columns=['one','two','three'])#,
               #index=list("abcde"))
print(mydf)
# DataFrame 객체 내용 선택(접근) 문법
# 라벨인덱스로 접근 ==> 라벨 인덱서  ==> loc  ( 라벨 location )
# 수치인덱스로 접근  ==>수치 인덱서  ==> iloc ( integer location )
print( mydf.iloc[ [1,3], : ] )
print( mydf.loc[ 2, 'two']) # 명시적 인덱스 2 를 라벨로 인식해서 loc가 가능
#print( mydf.loc[ 'c' , 'two'])
print("="*80)
print(mydf)
# 새로운 'four' 라는 컬럼을 추가
# 데이터는 나중에 추가
mydf['four'] = np.nan # 엑셀의 빈칸 표현 ==> 결측치 ( Not a Number )
print(mydf)

# 새로운 행 추가
mydf.loc[5] = np.nan
print(mydf.index)
print(mydf)
#mydf.to_excel("mydata.xlsx", index=False) # 엑셀로 저장