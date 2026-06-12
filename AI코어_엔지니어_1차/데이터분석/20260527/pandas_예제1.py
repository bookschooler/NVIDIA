import numpy as np
import pandas as pd

# 판다스 ==> 넘파이 상위 라이브러리, 데이터분석에 특화된 라이브러리
# ==> 판다스는 두가지 객체를 지원 ==> 1차원배열 형태 ( Series 객체 )
# ==> 2차원 배열 형태를 DataFrame 객체
# 넘파이 2차원 배열을 접근할때는 항상 수치 인덱스만 접근이 가능
# 판다스는 수치와 라벨(문자열) 인덱스도 지원을 해줌
# DataFrame 객체를 생성할때 여러 객체를 전달해서 생성할수 있음

# 1. 사전 객체를 전달해서 DataFrame 객체를 생성하는 문법
# 행, 열  인덱스에서 보이는 인덱스 ==> 명시적 인덱스
# 보이지 않는 인덱스 ==> 암묵적 인덱스
mydf = pd.DataFrame( { "kor":[50,60,70],"Eng":[80,90,77] },
                       index=["abc",'bef','hij'])  # DataFrame 객체 생성  ===> 2차원배열 형태
print(mydf)
print(mydf.columns) # 현 데이터프레임 객체의 Column 인덱스를 반환
# dtype='object'  ==> object 이면 문자열을 의미
# 데이터프레임 객체 생성시 인덱스를 부여하지 않으면 자동 인덱스이 동작
# 자동인덱스는 정수(수치) 범위 인덱스가 동작
print(mydf.index) # 행인덱스를 반환
print(mydf.values, type(mydf.values) ) # 데이터프레임 객체의 내용물을 반환
print(mydf , type(mydf) )
print("="*80)
print(mydf)
print(mydf['kor'])
# DataFrame 객체의 한 컬럼열을 선택하면 해당 객체는 1차원 형태인 Series 객체가 됨
print( type(mydf['kor']) ) # Series 클래스의 객체
print("="*80)
print(mydf)
# 컬럼 인덱스 수정
#mydf.columns[0] = '국어'
mydf.columns = ['국어','영어']  # 컬럼인덱스를 수정하는 문법
print(mydf)

# 2.리스트를 활용해서 DataFrame 객체를 생성
mydf = pd.DataFrame( [ [60,80,70],[90,50,85],[66,77,88] ] , columns=["국어","영어","수학"] ,
                     index=list("abc"))
print(mydf)
# 컬럼은 ==> 국어, 영어, 수학
# 행 ==> a, b, c


# 3.넘파이 배열을 활용한 DataFrame 객체생성

mydf = pd.DataFrame(  np.arange(10,25).reshape( (5,3)) , columns=['one','two','three'],
               index=list("abcde"))
print(mydf)

