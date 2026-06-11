from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt  # 1등: matplotlib 라이브러리 안에 있는 pyplot을 plt라는 별명으로 불러와줘!

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터셋 불러오기
homedf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260610/BostonHousing.csv')
print(homedf.info())
print(homedf.shape)

# X, Y 데이터로 나누기
x = homedf.iloc[:, :-1]
y = homedf.iloc[:, -1]

# train / test 데이터셋으로 나누기
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.3, random_state=42)

# feature들이 상이하면 정규화 해주기! 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_x)
test_scaled = scaler.transform(test_x)

# 딥러닝 뼈대 만들어주기 => Sequential
lin_model = Sequential()

# 입력층, 은닉층, 출력층 만들기 
# lin_model.add(Input(shape=(1,)))
lin_model.add( Dense( units = 30, input_dim = 13, activation= 'leaky_relu' ))
lin_model.add( Dense( units = 6, activation= 'leaky_relu' ))
lin_model.add( Dense( units = 1, activation= 'linear'))

# 뼈대 잘 만들었나 확인! summary
lin_model.summary()

# fit 전 환경설정 해주기
lin_model.compile( loss = 'mse' , optimizer = 'adam', metrics = ['accuracy', 'mae'] )

# #  학습 전 가중치(w) 확인해보기     => ⭐이게 레이어가 많은데 [0] 말고도 여러 레이어의 가중치를 다 확인해봐야하나 ? 
# weights = lin_model.layers[0].get_weights()
# print(weights)

# 학습(fit) 시키기
lin_model.fit( train_scaled, train_y ,  batch_size = 8,  epochs = 500, verbose = 1)

# 예측하기
pred = lin_model.predict(test_scaled)
print(pred)
print('='*80)
print(train_y[:5])

# #  학습 후 가중치(w) 확인해보기
# weights = lin_model.layers[0].get_weights()

sort_idx = np.argsort(train_scaled.flatten())
train_scaled_sorted = train_scaled[sort_idx]
pred_sorted = pred[sort_idx]

# 성능평가
print( lin_model.evaluate(test_scaled, test_y) )

# 결과 scatter plot이랑 회귀선 출력 
plt.plot(train_scaled, train_y, label='data')

# 가중치를 이용한 선형회귀 선을 표시
plt.plot(train_scaled, train_y, label='pred')
plt.legend() #label을 차트에 표시
plt.savefig('linear_model3.jpeg')
