from tensorflow.keras.datasets import imdb
import numpy as np

# 1. 데이터 준비
(train_x, train_y ), ( test_x , test_y ) = imdb.load_data(num_words = 1000) #어떤 단어를 어떤 수치로 변환했는지에 대한 정보
print(len(train_x)) # 25000
print(len(test_x))  # 25000
print(train_x[0])
print(test_x[0])
print(np.unique(train_y, return_counts = True)) # 라벨(정답)도 수치형으로 변환되어 있음

# 타깃이진분류 : 0(부정)  , 1(긍정) => 각 12500씩 
# train_x => 정수벡터화 되어있음

word_index = imdb.get_word_index()
print(word_index)

for word, idx in word_index.items():
    # print(word_index)
    if idx == 1:
        print(word)

conv_word_index =dict( [ (idx+3, word) for (word, idx) in word_index.items() ] )
print(conv_word_index)

# # for word, idx in conv_word_index.items():
# #     # print(word_index)
# #     if word_index == 4:
# #         print(word)

# # ⭐ 잘 이해 안감
# decode_sentence = ' '.join([ conv_word_index[i] if i in conv_word_index else'?' for i in train_x[0]])
# # print(decode_sentence)

# 데이터 x, y로 나누기
from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, test_size=0.2, random_state=43)
print(len(train_x))
print(len(val_x))

# 1차 ==> 길이가 다른 리뷰 정수데이터를 배열을 길이가 동일한 정수 배열로 변경 
from tensorflow.keras.preprocessing.sequence import pad_sequences
np.set_printoptions(threshold=np.inf, precision=8, suppress=True)

# 데이터에 Padding 넣어주기 (전처리)
train_seq = pad_sequences(train_x, maxlen = 100)
# print(train_seq)
print(len(train_seq[0]))
print(train_seq.shape)

val_seq = pad_sequences(val_x, maxlen = 100)
print(len(val_seq[0]))
print(val_seq.shape)

# 입력 데이터 원-핫 인코딩
from tensorflow.keras.utils import to_categorical
train_encoded = to_categorical(train_seq)
val_encoded = to_categorical(val_seq)

print(train_encoded.shape)
print(val_encoded.shape)    # 원-핫 인코딩 잘 됐나 확인
# print(train_encoded[0])

# RNN 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam

rnn_model = Sequential()

rnn_model.add( Input(shape = (100,) ) )       # 👉 Input shape = (문장 길이, 단어 표현 차원) = (100, 500)
rnn_model.add ( SimpleRNN (8) )
rnn_model.add ( Embedding( input_dim=500, output_dim=embeding_dim, ))
rnn_model.add ( Dense (1, activation='sigmoid') )
rnn_model.summary()

# # 모델 컴파일
# import tensorflow as tf
# opt = tf.keras.optimizers.Adam(learning_rate = 1e-6)
# rnn_model.compile(loss = "binary_crossentropy" , 
#                   optimizer = opt, metrics = ['accuracy'])

# # 콜백 지정
# from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
# checkpointer_cb = ModelCheckpoint('./imdb_bestmodel.keras', save_best_only=True )
# earlystop_cb = EarlyStopping(patience=3, restore_best_weights=True)

# # 모델 학습
# record = rnn_model.fit(train_encoded, train_y, batch_size = 64, epochs=100, verbose=1,   
#         validation_data = (val_encoded, val_y), callbacks = (checkpointer_cb, earlystop_cb))

# # 시각화 해보기

# import matplotlib.pyplot as plt
# plt.plot(record.history['loss'], label='loss') # 훈련 손실
# plt.plot(record.history['val_loss'], label='val_loss') # 검증 손실
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend(loc='best')
# plt.savefig('imdb.jpeg')




# # best 모델 로드하기
# from tensorflow.keras.models import load_model
# model = load_model('imdb_bestmodel.keras') 

# # 예측해볼 데이터 준비
# ex_review = "I gave this movie 5 stars because it perfectly cured my insomnia. \
# The special effects look like they were made on a 10-year-old smartphone, \
# and the actors deliver their lines with the emotion of a brick wall. \
# If you enjoy staring at a blank screen for two hours, this absolute masterpiece is for you."

# # 준비 데이터 정규화로 정제
# import re
# trimmed_review = re.sub('[^0-9a-zA-Z\s]','',sentence_arg).lower()

# # 인코딩 규칙 정하기
# word_to_index = imdb.get_word_index() # <=== imdb 인덱스 매핑 사전 반환
# for key, value in word_to_index.items():
#         if value == 1:
#                 print('key , value :',key, value) # key , value : the 1
# print(word_to_index['this']) # 11로 정수매핑 되있지만 --> 정수 토큰화된 내용은 14

# encoded = [ ]
# for word in ex_review.split(' '):
# # 단어집합 크기를 훈련데이터와 동일하게 500으로제한
#         try:
#                 if word_to_index[word] <= 500: 
#                         encoded.append( word_to_index[word]+3 ) # 예) 'the'의 value값 1 에 3을 더해 4를 저장
#                 else:
#                         # 500 이상의 숫자는 <untoken> 알수없는 토큰으로취급
#                         encoded.append(2)

# # 단어 집합에 없는 단어, 즉 word_to_index 단어 사전에 word 키 값이 없는경우
# # <untoken> 알수없는 토큰으로 취급
#         except KeyError:
#                 encoded.append(2)

# # 인코딩 한 리뷰 문장을 padding 처리해주기
# # 훈련,테스트데이터와동일하게길이를 100으로패딩(타임스템프크기)
# # 예측

# pad_new = pad_sequences( [encoded], maxlen= 100 ) # 타임스템프형성을 위한2차원배열형태전달

# print(pad_new)
# score = float( model.predict(pad_new) )
# print('score : ', score)
# if(score > 0.5):
#         print("{:.2f}% 확률로 긍정 리뷰".format(score*100))
# else:
#         print("{:.2f}% 확률로 부정 리뷰".format((1-score) * 100))
