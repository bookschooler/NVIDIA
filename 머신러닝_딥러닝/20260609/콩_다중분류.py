import numpy as np
import pandas as pd

# 데이터셋 불러오기
np.set_printoptions(precision = 8, suppress = True)
beandf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260609/Dry_Bean.csv')

# 데이터 특성 대략적으로 확인
print(beandf.head(5))
print(beandf.shape)
print(beandf.info())

# 데이터 series를 numpy 배열로 바꿔주기
bean_target = beandf['Class'].to_numpy()
print(beandf['Class'].unique())
print(beandf.columns)
bean_features = beandf[['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength',
       'AspectRation', 'Eccentricity', 'ConvexArea', 'EquivDiameter', 'Extent',
       'Solidity', 'roundness', 'Compactness', 'ShapeFactor1', 'ShapeFactor2',
       'ShapeFactor3', 'ShapeFactor4']].to_numpy()  #⭐ 대괄호 두 개!!! [ [] ]

print(bean_target)
print(bean_features)

# train/test 데이터로 분리하기
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(bean_features, bean_target, random_state=42)

print(train_x.shape)
print(test_x.shape)

# feature들에 대한 표준 정규화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_x)
test_scaled = scaler.transform(test_x)
print(test_scaled[:5])

# 학습 모델 불러오기
from sklearn.linear_model import LogisticRegression
multi_rlmodel = LogisticRegression(multi_class='multinomial', max_iter = 1000)


# 학습시키기
multi_rlmodel.fit(train_scaled, train_y)

# 성능평가
print(multi_rlmodel.score(train_scaled, train_y))
print(multi_rlmodel.score(test_scaled, test_y))

# 예측 해보기

pred = multi_rlmodel.predict( train_scaled[:2] )
print(pred)
proba = multi_rlmodel.predict_proba ( train_scaled[:2] )
print(proba)

max_indices = np.argmax(proba, axis=1)

for i, idx in enumerate(max_indices):
    pred_label = multi_rlmodel.classes_[idx]
    pred_prob = proba[i][idx]
    print(
        f"데이터 {i+1}: 가장 높은 확률은 {pred_prob*100:.2f}% 이며, 해당 레이블은 '{pred_label}' 입니다."
    )


