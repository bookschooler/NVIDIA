from tensorflow.keras.datasets import imdb
import numpy as np

(train_x, train_y ), ( test_x , test_y ) = imdb.load_data(num_words = 500) #어떤 단어를 어떤 수치로 변환했는지에 대한 정보
print(len(train_x)) # 25000
print(len(test_x))  # 25000
print(train_x[0])
print(test_x[0])
print(np.unique(train_y, return_counts = True)) # 라벨(정답)도 수치형으로 변환되어 있음

# 타깃이진분류 : 0(부정)  , 1(긍정) => 각 12500씩 
# train_x => 정수벡터화 되어있음

word_index = imdb.get_word_index()
# print(word_index)

for word, idx in word_index.items():1
    # print(word_index)
    if idx == 1:
        print(word)

# conv_word_index =dict( [ (idx+3, word) for (word, idx) in word_index.items() ] )
# print(conv_word_index)

# for word, idx in conv_word_index.items():
#     # print(word_index)
#     if word_index == 4:
#         print(word)

# decode_sentence = ''.join([ conv_word_index[i] if i in conv_word_index else'?' for i in train_x[0]])
# print(decode_sentence)

from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = train_test_split(train_x, train_y, test_size=0.2, random_state=43)
print(len(train_x))
print(len(val_x))

# 1차 ==> 길이가 다른 리뷰 정수데이터를 배열을 길이가 동일한 정수 배열로 변경 
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_seq = pad_sequences(train_x, maxlen = 100)
print(len(train_seq[0]))
print(train_seq.shape)

val_seq = pad_sequences(val_x, maxlen = 100)
print(len(val_seq_seq[0]))
print(val_seq.shape)


