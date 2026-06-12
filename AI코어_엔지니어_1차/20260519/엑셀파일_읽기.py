
import pandas as pd

mydf = pd.read_excel("MyDf.xlsx" , index_col=0)  # 엑셀 파일의 내용을 읽어서 DF객체로 변환
print(mydf)