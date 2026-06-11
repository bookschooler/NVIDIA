import numpy as np
import pandas as pd

# e 지수 표현하는 과학적 표기 대신 소수점 이하 8자리까지 표현해라~   
# e의 몇승 이렇게 표시하는 걸 과학적 표기라 함

np.set_printoptions(precision=8, suppress=True)
fishdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260609/fish_data.csv')
print(fishdf)
print(fishdf.info())
print(fishdf.shape)
print(fishdf['Species'].unique())

print(fishdf.isnull().sum())
print(fishdf.isnull().sum(axis=1))

#Series 를 넘파이 배열로 변환해주는 메서드 ==> to_numpy()
fish_target = fishdf['Species'].to_numpy()
print(fish_target)
print(fishdf.columns)
fish_train = fishdf[ ['Weight', 'Length', 'Diagonal', 'Height', 'Width'] ].to_numpy()
print(fish_train)


# train데이터와 test데이터 분리하기

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(fish_train, fish_target, random_state=42)

print(train_x.shape)
print(test_x.shape)

# 스케일 조정 (표준점수 정규화) ==> 스케일 정규화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_x)

test_scaled = scaler.transform(test_x)
print(train_scaled[:5])

# 학습모델 준비
# sklearn 다중분류 => 로지스틱 회귀 모델에서 특정 파라미터 설정만 해주면 됨
from sklearn.linear_model import LogisticRegression
multi_lrmodel = LogisticRegression(multi_class='multinomial', max_iter=1000, C=20) 

# 학습(fit)
print(train_y)  # 0001
multi_lrmodel.fit(train_scaled, train_y)

# 성능평가
print(multi_lrmodel.score(train_scaled, train_y))
print(multi_lrmodel.score(test_scaled, test_y)) #0.925성능

# 예측
# 테스트 데이터 중 첫번째 데이터 하나만 어떤 종인지 예측
print( test_scaled[:3].shape )
pred = multi_lrmodel.predict(test_scaled[:3])   #[0] 으로 하면 1차원이라 꼭 [: 1] 슬라이싱으로 해야함.
print(pred)


print( multi_lrmodel.predict_proba( test_scaled[:1] ) )
print( multi_lrmodel.classes_)
