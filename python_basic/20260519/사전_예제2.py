import pandas as pd

scoredict = {"kor": [80, 69, 70], "eng": [77, 88, 99], "math": [55, 66, 77] }
print(scoredict)

mydf = pd.DataFrame(scoredict)
print(mydf)

mydf.to_excel("MyDf.xlsx")
