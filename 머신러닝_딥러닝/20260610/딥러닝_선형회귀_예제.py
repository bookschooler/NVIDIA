from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 10, 10)
print(X)
print(X.shape, type(X.shape))

# Y = X + np.random.randn(*X.shape)
# print(Y)

# # 딥러닝 선형회귀 모델 설계
# # 입력데이터(x)는 1개씩 들어감
# # 입력층의 뉴런은 1개 
# # 출력층의 활성화 함수는 linear 선형함수
# # 손실함수 : MSE

# linear_model = Sequential() # 모델 설계 틀 준비
# linear_model.add(Dense(units=1, input_dim = 1, activation='linear', use_bias=False))    # 일단 편향 무시하겠단 뜻
# # 은닉층이 없고 이게 출력층까지 되니깐 활성화함수 넣어줌
# linear_model.summary()

# # 모델 사용할 준비과정 ==> compile (환경설정)
# linear_model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

# # 학습 전, 가중치(w) 체크해보기
# weights = linear_model.layers[0].get_weights()
# w = weights[0][0][0]
# print(weights)
# print('fit 전 가중치 체크: ', w)

# # 학습(fit)
# linear_model.fit(X, Y, batch_size = 1, epochs=1000, verbose=1)

# # 학습 완료 후의 가중치(w) 체크해보기
# weights = linear_model.layers[0].get_weights()
# print(weights)
# w = weights[0][0][0]
# print('fit 완료 후 가중치 체크: ', w)

# # 시각화 해보기
# plt.plot(X, Y, label='data')

# # 모델이 찾은 선형회귀선을 표시
# plt.plot(X, w*X, label='pred')
# plt.legend()    # label을 차트에 뿌려라
# plt.savefig('linear_model.jpeg')