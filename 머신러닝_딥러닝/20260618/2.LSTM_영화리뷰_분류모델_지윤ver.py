from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np

(train_x, train_y), (test_x, test_y) = imdb.load_data(num_words = 5000)  # imdb는 4개를 반환하는데 안쓸 거면 _ 로 표현하면 반환되지 않음 (train_y, test_x, y 임)
# 숫자를 500까지만 사용함, 빈도수가 낮은 것(숫자였던것)은 2로 채워짐.
# print(len(train_x))   # 25000개
# print(len(test_x))   # 25000개. 둘다
# print(train_x[0])  # 오! 문자열이 정수벡터화 되어 있음 
# 문장의 시작은 1, 가장 많이 나온 단어는 4, 미사용(특별 토큰)하는 수 3, 0은 패딩 과 같은 패턴이 존재함
# tokenizer 의 기능을 내부적으로 수행하여 단어집합 형성과 빈도수에 따른 정수 자동 매핑

# 타깃 이진 분류 : 0(부정), 1(긍정)
print(train_y[0])  # 라벨(정답지)도 수치형으로 변환되어 있음. 
print(np.unique(train_y, return_counts = True))  # [0, 1](긍정, 부정)이 [12500, 12500]개씩 존재함

# test 데이터는 성능 test에 온전하게 사용하기 위해 val을 따로 분리
train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, test_size=0.2, random_state=42)
# print(len(train_x))  # 20000 개 
# print(len(val_x))  # 5000 개 

# 각각의 문장(데이터)들을 길이가 100인 정수 벡터로 맞춰줘야함 ( 데이터셋 길이를 표로 시각화했을때 100개정도가 가장 많기 때문.. )
# 1차 ==> 길이가 다른 리뷰 정수데이터 배열을 길이가 동일한 정수데이터 배열로 변경 ( 긴거는 버리고, 짧은거는 0으로 패딩 생성 )
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_seq = pad_sequences(train_x, maxlen = 100)
# print(len(train_seq[0]))  # 길이 100이 됨
# print(train_seq[5645])

val_seq = pad_sequences(val_x, maxlen = 100)
# print(len(val_seq[0]))  

test_seq = pad_sequences(test_x, maxlen = 100)
# print(len(test_seq[0]))  


# LSTM 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, Dense, Dropout

embedding_dim = 100 # embedding 밀집벡터 차원
hidden_units = 128 # LSTM 뉴런수

rnn_model = Sequential()
rnn_model.add(Embedding(input_dim=5000, output_dim=embedding_dim, input_length=100))  
# rnn_model.add(SimpleRNN(8))  # 뉴런 8개 일때 이 층 가중치 200개.
rnn_model.add(LSTM(hidden_units))  # LSTM 층 뉴런 128개 , 뉴런 8개일때 이 층 가중치 800개, simpleRNN보다 가중치가 4배 늘어남.
rnn_model.add(Dropout(0.3))
rnn_model.add(Dense(1, activation='sigmoid'))

rnn_model.build(input_shape=(None, 100))  # keras 버전 올라가면서 Embedding layer 만으로는 모델 생성이 안댐.

rnn_model.summary()

# 모델 컴파일
import tensorflow as tf
optimizer = tf.keras.optimizers.Adam(learning_rate = 1e-3)
rnn_model.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])

#모델 학습 
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint_cb = ModelCheckpoint('./LSTM_IMDB_bestmodel.keras', save_best_only=True)
earlystopping_cb = EarlyStopping( patience=5, restore_best_weights=True)

history = rnn_model.fit(train_seq, train_y, batch_size = 128, epochs = 200, verbose = 1,
                        validation_data = (val_seq, val_y),
                        callbacks = [checkpoint_cb, earlystopping_cb])

# 성능 평가 
print('test acc:', rnn_model.evaluate(test_seq, test_y) )

# RNN과 같은 조건(뉴런수, 임베딩 차원)일 때: accuracy: 0.8630 - loss: 0.3264 - val_accuracy: 0.8514 - val_loss: 0.3485 , test_acc: 0.8456
# 약간 성능이 좋아짐. 2%p정도.

