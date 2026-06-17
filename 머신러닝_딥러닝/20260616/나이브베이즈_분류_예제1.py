import pandas as pd
from sklearn.datasets import load_iris  #붓꽃 데이터셋 <= 가우시안 써볼라고 사용 
from sklearn.model_selection import train_test_split # train/test 분리할 때 사용


from sklearn.naive_bayes import GaussianNB  # 데이터 특징이 정규분포일 때 분류 모델로 사용! 
# 분류 모델 => GaussianNB
from sklearn import metrics # 혼동행렬 
from sklearn.metrics import accuracy_score # 정확도
# score 메소드가 다 해주긴 하지만 그래도 직접적으로 보려면 import하는 게 ... 

dataset = load_iris()
print(dataset)

irisdf = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
print(irisdf)
irisdf['target'] = dataset['target']
print(irisdf)

# 타겟을 시각화 하기 위해 
# 0 => 'setosa',  1=> 'versicolor' , 2 => 'virginica'
irisdf['target'] = irisdf['target'].map({0:'setosa', 1:'versicolor', 2:'virginica'})
print(irisdf)


# Setosa DF
# Versicolor DF
# Virginica DF  로 쪼개보기

setosa_df = irisdf.loc[irisdf['target'] == 'setosa'].copy()     # target이 setosa인 애만 복사해서 df로 만들기
versicolor_df = irisdf.loc[irisdf['target'] == 'versicolor'].copy()
virginica_df = irisdf.loc[irisdf['target'] == 'virginica'].copy()

print(setosa_df)
print(versicolor_df)
print(virginica_df)

# 시각화 해보기
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 3, figsize = (15,7) )

sns.histplot(data=setosa_df, x='sepal length (cm)', kde=True, ax = axes[0])
sns.histplot(data=versicolor_df, x='sepal length (cm)', kde=True, ax = axes[1])     # => 이렇게 시각화 해보는 걸 통해 데이터가 가우시안 분포를 보인다는 걸 확인✅
sns.histplot(data=virginica_df, x='sepal length (cm)', kde=True, ax = axes[2])

plt.savefig('iris_histplot.jpeg')
