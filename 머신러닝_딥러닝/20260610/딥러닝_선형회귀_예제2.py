import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#농어길이데이터 ( 캐글Fish Market 데이터참조)
perch_length=np.array([8.4,13.7,15.0,16.2,17.4,18.0,18.7,19.0,19.6,20.0,21.0,
21.0,21.0,21.3,22.0,22.0,22.0,22.0,22.0,22.5,22.5,22.7,
23.0,23.5,24.0,24.0,24.6,25.0,25.6,26.5,27.3,27.5,27.5,
27.5,28.0,28.7,30.0,32.8,34.5,35.0,36.5,36.0,37.0,37.0,
39.0,39.0,39.0,40.0,40.0,40.0,40.0,42.0,43.0,43.0,43.5,
44.0])
# 농어무게데이터 (캐글FishMarket 데이터참조)
perch_weight=np.array([5.9,32.0,40.0,51.5,70.0,100.0,78.0,80.0,85.0,85.0,110.0,
115.0,125.0,130.0,120.0,120.0,130.0,135.0,110.0,130.0,
150.0,145.0,150.0,170.0,225.0,145.0,188.0,180.0,197.0,
218.0,300.0,260.0,265.0,250.0,250.0,300.0,320.0,514.0,
556.0,840.0,685.0,700.0,700.0,690.0,900.0,650.0,820.0,
850.0,900.0,1015.0,820.0,1100.0,1000.0,1100.0,1000.0,
1000.0])


# 농어 길이 / 농어 무게 를  train/test 데이터로 분리

train_x, test_x, train_y, test_y = \
    train_test_split(perch_length, perch_weight, random_state=42)

print(train_x.shape, test_x.shape)
# 1차원 =--> 2차원으로 변경
train_x = train_x.reshape(-1,1)
test_x = test_x.reshape(-1,1)
print(train_x.shape, test_x.shape)
print(train_x)
# # 길이(x)에 제곱한  특성을 추가
# # x*2
# # print( train_x[:5] )
# # print( train_x[:5]**2 )
      
train_poly = np.column_stack( (train_x**2, train_x))
print(train_poly[:5])
print(train_poly.shape)
test_poly = np.column_stack( (test_x**2, test_x))
print(test_poly.shape)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train_scaled = scaler.fit_transform(train_poly)
test_scaled = scaler.transform(test_poly)


# 딥러닝 선형회귀 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# 입력 feature 2개, 입력층의 뉴런 개수 4개 => 다음 은닉층 뉴런 개수 8개 => 출력층 뉴런 개수 1개
# 모델 틀 준비 Sequential
lin_model = Sequential()
lin_model.add(Dense(units=4, input_dim = 2, activation = 'leaky_relu'))     # 얘가 layer[0]이자 입력 데이터 받는 입력층
# units = 각 층의 뉴런 개수, input_dim은 입력층에서 받는 입력 feature 개수 
lin_model.add(Dense(units=8, activation='leaky_relu'))                      # 얘가 layer[1]
lin_model.add(Dense(units=1, activation='linear'))

# 모델 summary()
lin_model.summary()

# 모델 compile() => 이제 모델 학습 전 최종적으로 설정같은 거 마무리 짓는 단계
lin_model.compile(loss='mse', optimizer='adam', metrics=['mae'])

# # 학습 전 가중치(w) 확인해보기
# weights = lin_model.layers[0].get_weights()
# w1 = weights[0][0][0]
# w2 = weights[0][0][1]
# print(w1)
# print(w2)
# print(f'fit 전 가중치: ', w1, w2)

# print("진짜 데이터 모양:", train_x.shape)

# 모델 학습(fit)
lin_model.fit(train_poly, train_y, batch_size = 1, epochs=500, verbose=1)
print(lin_model.evaluate(test_poly, test_y))

# 학습된 모델로 예측하기
pred = lin_model.predict(train_poly[:5])
print(pred)
print('='*80)
print(train_y[:5])

#  학습 후 가중치(w) 확인해보기
weights = lin_model.layers[0].get_weights()

sort_idx = np.argsort(train_x.flatten())
train_x_sorted = train_x[sort_idx]
pred_sorted = pred[sort_idx]


# 성능평가
print( lin_model.evaluate(test_poly, test_y) )

# 결과 scatter plot이랑 회귀선 출력 
# plt.scatter(train_poly, pred)
plt.plot(train_scaled, train_y, label='data')

# 가중치를 이용한 선형회귀 선을 표시
plt.plot(train_x[sort_idx], pred[sort_idx], label='pred')
plt.legend() #label을 차트에 표시
plt.savefig('linear_model2.jpeg')
