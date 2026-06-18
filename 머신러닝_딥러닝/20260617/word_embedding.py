import numpy as np
from tensorflow.keras.layers import Embedding

input_data = np.array([
[3,4,7],
[9,2,3],
[1,6,499]
])

embedding = Embedding(input_dim=500, output_dim=16, input_length = 100)
oupout = embedding(input_data)
print(oupout)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, SimpleRNN,Dense

rnnmodel = Sequential()
input = Input( shape=(100, ))
rnnmodel.add(input)
rnnmodel.add ( Embedding (500, 16, input_length=100) )  # 이게 입력층이 됨
rnnmodel.add ( SimpleRNN (8))
rnnmodel.add ( Dense(1, activation='sigmoid'))
rnnmodel.summary()
