from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN
import numpy as np

# 1. 데이터
x = np.array([[5,6,7], [1,2,3], [11,12,13], [6,7,8]])
y = np.array([8,4,14,9])

print(x)
print(x.shape)
x = x.reshape(4,3,1) # (3 timesteps, 1 입력 차원수) ==> 4개의 샘플
print(x)

rnn_model = Sequential()
rnn_model.add(SimpleRNN(10, return_sequences=False, input_shape=(3,1))) # 3개 timesteps , 1 입력차원수
# input_shape = ((batch_size) , timesteps, features)  
rnn_model.add(Dense(1)) # default : linear , 별도 활성화함수 없이 입력 뉴런과 가중치 계산결과가 그대로 출력
rnn_model.summary()

# 모델 컴파일
rnn_model.compile(loss = 'mse' , optimizer = 'adam' , metrics= ['mse'] )

# 모델 학습
rnn_model.fit(x, y, epochs = 1000, batch_size = 1)    # 데이터가 작아서 1000으로 한거임.

# 모델 학습
print(rnn_model.predict(x))

# 성능 측정
rnn_model.evaluate(x, y)

# 임의의 데이터 예측
temp_data = np.array([6,7,8])
temp_data = temp_data.reshape((1,3,1))

pred1 = rnn_model.predict(temp_data)
print(pred1)