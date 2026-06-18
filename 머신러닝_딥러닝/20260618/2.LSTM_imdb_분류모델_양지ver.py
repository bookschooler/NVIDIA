from tensorflow.keras.datasets import imdb
import numpy as np

(train_x, train_y ), ( test_x , test_y ) = imdb.load_data(num_words=500) #어떤 단어를 어떤 수치로 변환했는지에 대한 정보
print(len(train_x))
print(len(test_x))
print(train_x[0])
print(np.unique(train_y, return_counts=True))  # 라벨도 수치형으로 변환되어있음

from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = \
    train_test_split(train_x, train_y, test_size=0.2, random_state=48)
print(len(train_x)) #2000
print(len(val_x)) #5000

print(len(train_x[0]))
print(len(train_x[1]))

#리뷰문장 길이시각화 (꼭 나중에 해봐)

# PADDING 주기 
from tensorflow.keras.preprocessing.sequence import pad_sequences
#길이를 100으로 변경할때 짧은거는 0으로 채우고 긴거는 버린다.

train_seq = pad_sequences(train_x, maxlen =100)
print(len(train_seq[0]))
print(train_seq.shape)
print(train_seq[400])

val_seq = pad_sequences(val_x, maxlen =100)
print(len(val_seq[0]))
print(val_seq.shape)


# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, SimpleRNN, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

embedding_dim = 16 # embedding 밀집벡터 차원
hidden_units = 8 # LSTM 뉴런 수

rnnmodel = Sequential()
rnnmodel.add(Input(shape=(100,)))
rnnmodel.add( Embedding (input_dim = 500, output_dim= embedding_dim))
rnnmodel.add(LSTM(hidden_units))
rnnmodel.add(Dense(1, activation='sigmoid'))
rnnmodel.summary()

# 모델 컴파일
import tensorflow as tf

optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4) # 더 자세하게 파라미터 조정하기 위해서! 

rnnmodel.compile(optimizer=optimizer, metrics=['accuracy'], loss= 'binary_crossentropy')

# CALLBACK 조건 만들기 
early_stopping_cb = EarlyStopping(patience =5, restore_best_weights= True)
checkpoint_cb = ModelCheckpoint('./rnn_model.keras')

# 모델 학습
record = rnnmodel.fit(train_seq, train_y, epochs=200, 
                       batch_size=16,validation_data=(val_seq, val_y),
                       callbacks= [checkpoint_cb, early_stopping_cb])