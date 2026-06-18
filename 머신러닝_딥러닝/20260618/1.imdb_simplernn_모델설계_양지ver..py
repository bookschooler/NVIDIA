from tensorflow.keras.datasets import imdb
import numpy as np

(train_x, train_y ), ( test_x , test_y ) = imdb.load_data(num_words=1000) # 어떤 단어를 어떤 수치로 변환했는지에 대한 정보
# num_words = 1000 => 자주 사용하는 단어 1000개만 사용하겠다
print(len(train_x))
print(len(test_x))
print(train_x[0])
print(np.unique(train_y, return_counts=True)) # 라벨도 수치형으로 변환되어있음

# test / val 데이터셋으로 분류
from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = \
    train_test_split(train_x, train_y, test_size=0.2, random_state=48)
print(len(train_x)) #20000
print(len(val_x)) #5000

print(len(train_x[0]))
print(len(train_x[1]))

# # 리뷰 문장 길이시각화 (꼭 나중에 해봐)



# Padding 주기 => 길이가 다른 정수데이터 배열을 길이가 동일한 정수 배열로 변경 
from tensorflow.keras.preprocessing.sequence import pad_sequences
# 길이를 100으로 변경할 때 짧은거는 0으로 채우고 긴거는 버린다.

train_seq = pad_sequences(train_x, maxlen=200)
print(len(train_seq[0]))
print(train_seq.shape)
# print(train_seq[400])

val_seq = pad_sequences(val_x, maxlen =200)
print(len(val_seq[0]))
print(val_seq.shape)

# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, SimpleRNN, Dense 
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

rnnmodel = Sequential()
rnnmodel.add(Input(shape=(100,)))  # 문장 길이
rnnmodel.add(Embedding(input_dim=1000, output_dim= 16)) # 총 단어 수 = input_dim,  output_dim = 차원수(벡터) 
rnnmodel.add(SimpleRNN(16))
rnnmodel.add(Dense(1, activation='sigmoid'))
rnnmodel.summary()

# 모델 컴파일
import tensorflow as tf

optimizer = tf.keras.optimizers.Adam(learning_rate = 1e-4)  
# 옵티마이저 learning_rate 조정때문에 따로 빼줌. 

# Adam의 파라미터들 
# m = beta_1 * m + (1-beta_1) * gradient
# beta_1 이라는 파라미터도 있음! => beta_1 = 0.9 => 과거 기록을 0.9만큼 유지 
# learning_rate	한 번에 얼마나 이동할지
# beta_1	gradient 방향 기억
# beta_2	gradient 크기 기억
# epsilon	0으로 나누는 것 방지

rnnmodel.compile(loss= 'binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
early_stopping_cb = EarlyStopping(patience =3, restore_best_weights= True)
checkpoint_cb = ModelCheckpoint('./rnn_model.keras')
record = rnnmodel.fit(train_seq, train_y, epochs=200, batch_size=16,
                       validation_data=(val_seq, val_y),
                       callbacks= [checkpoint_cb, early_stopping_cb])



# BEST 모델 불러와서 새로운 데이터 예측
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import vgg16
from tensorflow.keras.datasets import imdb

print('='*200)

# BEST 모델 소환
rnn_bestmodel = load_model('/home/sophie/tf_env/rnn_model.keras')

rnn_bestmodel.summary()

# 데이터 준비
(train_input, train_y), (test_input, test_y) = imdb.load_data(num_words=500)

# 패딩 넣어주기
from tensorflow.keras.preprocessing.sequence import pad_sequences
test_seq = pad_sequences(test_input, maxlen=100)
print(test_seq.shape) # (25000, 100) # test 데이셋도 길이 100으로 동일 padding
print(test_seq[0])
print('정확도 : %.4f ', rnn_bestmodel.evaluate(test_seq, test_y)[1])
print(rnn_bestmodel.predict(test_seq[0:1]))

# 단어 : 수치 확인? 
word_to_index = imdb.get_word_index()
for key, value in word_to_index.items():
    if value == 1:
        print('key , value :',key, value) # key , value : the 1
print(word_to_index['this'])

# 영화 문장 샘플
negative_review_str = 'A handsomely mounted thriller that almost works, which somehow makes its failures sting more. The lead shows flashes of real talent, yet the performance never quite settles into something you can hold onto. The cinematography has moments of genuine beauty, though it often tips into murk for its own sake, and the score swings between haunting and merely tiresome. The pacing starts strong before sagging badly in the middle, and the payoff, while competent, never delivers the punch it keeps promising. There is a better film buried in here somewhere. As it stands, it is watchable but hard to recommend. Wait for streaming.'
positive_review_str = 'A taut, gripping thriller that earns every minute of its runtime. The lead delivers a career-defining performance, balancing quiet vulnerability with sudden bursts of menace. The cinematography turns ordinary streets into something alive and electric, while the score hums beneath each scene like a held breath. Even the brief lull in the middle act builds tension that pays off beautifully. What stays with you is not the plot but the mood, a lingering charge that follows you out of the theater. Smart, stylish, and quietly devastating, this is filmmaking that respects its audience. Well worth seeing on the big screen.'

import re
def new_sentence_tokenization(sentence_arg):
    new_sentences = re.sub('[^0-9a-zA-Z\s]','',sentence_arg).lower()
    # re.sub(패턴, 바꿀문자, 대상문자열) , 리스트일 땐 안되고 문자열 일 때만 가능! 
    # map(함수, 반복가능한객체)



#     encoded= []
#     for word in new_sentences.split(' '):
#         try:
#             if word_to_index[word] <= 500:
#                 encoded.append(word_to_index[word]+3)
#             else:
#                 encoded.append(2)

#         except KeyError: encoded.append(2)

#     pad_new = pad_sequences([encoded], maxlen=100)
#     print(pad_new)

#     score = float(rnn_bestmodel.predict(pad_new))
#     print('score : ', score)

#     if(score > 0.5):
#         print("{:.2f}% 확률로 긍정 리뷰".format(score*100))
#     else:
#         print("{:.2f}% 확률로 부정 리뷰".format((1-score) * 100))

# new_sentence_tokenization(negative_review_str) # 함수 호출
# new_sentence_tokenization(positive_review_str) # 함수 호출