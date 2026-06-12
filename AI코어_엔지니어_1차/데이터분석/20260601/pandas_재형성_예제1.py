import numpy as np
import pandas as pd


mydf = pd.DataFrame([[80,90,70],[75,65,95]],
index = pd.Index(['kor','math'], name='subject'),
columns=pd.Index(['stu1','stu2','stu3'],name='student'))
print(mydf)
# 데이터프레임의 형태(모양)을 바꿀때 필요한 문법 ==> 재형성
stdf = mydf.stack()  # DF 객체 재형성
print(stdf, type(stdf))

unstdf = stdf.unstack()
print(unstdf)