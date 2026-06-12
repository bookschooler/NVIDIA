
import numpy as np
import pandas as pd

# 그룹핑 ==> groupby , pivot_table
# groupby연산 ==> 1.splite(분리)  2.apply(함수적용)  3.combine(결합)

df = pd.DataFrame( {"subject":['kor','eng','kor','eng','math','kor','math'],
                "score": [   70,   80,   90,   85,    75,   65,   60] } )
print(df)

# groupby연산 문법
#df.groupby(기준키)[집계(통계)함수를 적용할 컬럼선택].함수적용할집계(통계)함수명시

grp = df.groupby('subject')[['score']].sum()
# ['score'] ==> 집계(통계)를 적용할 컬럼을 리스트처럼 여러개로 선택 표현하면
# =-=> 결과물은 Dataframe로 만들어짐
print(grp)  # 그룹핑된 Series 객체가 반환

