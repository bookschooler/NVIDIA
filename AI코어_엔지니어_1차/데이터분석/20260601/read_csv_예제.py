import numpy as np
import pandas as pd

# 젤 위에 있는 데이터를 기본적으로 컬럼 데이터로 인식해서 Dataframe 형성
# header=None : 젤 위에 데이터를 컬럼으로 인식하지 않고 데이터로 사용
scoredf = pd.read_csv("scoredata.csv", names=['kor','eng','math','total'])
print(scoredf)