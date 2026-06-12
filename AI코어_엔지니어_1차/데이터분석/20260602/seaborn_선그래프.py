import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 시각화
import seaborn as sns # 시각화

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현


fig, axes = plt.subplots(2,1)
dateidx = np.arange(0,100,10)
data = np.random.randn(10,4).cumsum(axis=0)
print(data)

mydf = pd.DataFrame(data, index=dateidx, columns=list("ABCD") )
print(mydf)

sns.barplot(ax=axes[0], data=mydf )
sns.barplot(ax=axes[1], data=mydf['C'])

plt.show()