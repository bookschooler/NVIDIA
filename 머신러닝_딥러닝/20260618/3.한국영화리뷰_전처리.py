import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 50)

# train 데이터셋
train_df = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260618/train_stopwords_reviews.csv',
                      index_col = 0)  #⭐
print(train_df)
print(train_df.info()) #총 데이터 31968 / 리뷰 컬럼 31965

# test 데이터셋
test_df = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260618/test_stopwords_reviews.csv',
                      index_col = 0)  #⭐
print(test_df)
print(train_df.info()) 

# 결측치 있는 행 제거하기
train_df.dropna(how='any', inplace=True)
test_df.dropna(how='any', inplace=True)

print(train_df.info())
print(test_df.info())   # 총 데이터 31661

# 문자열 = 토큰화 (= 특정 단어를 수치로 매핑 치환)
from tensorflow.keras.preprocessing.text import Tokenizer
# 고정 길이에 맞춰 패딩 넣어주기 (= 고정길이 정수 벡터 생성할 때 )
from tensorflow.keras.preprocessing.sequence import pad_sequences

word_size = 11775   # imdb의 num_words 역할
tokenizer = Tokenizer(word_size)

tokenizer.fit_on_texts(train_df['document'])    # ⭐ .fit_on_text 뜻 조사
print(tokenizer.word_index) #⭐ .word_index 

# for word, idx in tokenizer.word_index.items():
#     if idx ==2:
#         print(word)

############################## 토크나이징 ######################### tokenizer.word_index 를 활용해서 리뷰 데이터를 정수 배열로 생성
print('='*200)
# # print( tokenizer.texts_to_sequences(train_df['document'])[:5] )
train_df['sequence'] = tokenizer.texts_to_sequences(train_df['document'])
print(train_df.head())
test_df['sequence'] = tokenizer.texts_to_sequences(test_df['document'])
print(test_df.head())

###################### Padding 넣어주기 ####################
train_df.reset_index(drop=True, inplace=True)  # 인덱스 초기화
test_df.reset_index(drop=True, inplace=True)   # 인덱스 초기화

print(train_df[25:30])
print(test_df[57:62])

# 11775 개 단어 집합만 고려 했음으로 빈도수가 1 이하인 단어로 이루어진 문장은 텅빈( [ ] )
# 형태로 변환 됨, 따라서 해당 문장의 인덱스를 찾아 제거 해줌
drop_train_idx = [idx for idx, sentence in enumerate(train_df['sequence']) if len(sentence) < 1]
print('drop_train_idx : \n', drop_train_idx)

drop_test_idx = [idx for idx, sentence in enumerate(test_df['sequence']) if len(sentence) < 1]
print('drop_test_idx : \n', drop_test_idx)

# 텅빈([ ]) sequence 데이터 위치 인덱스 활용해서  Dataframe 해당 행 삭제
train_df.drop(drop_train_idx,axis=0, inplace=True)
test_df.drop(drop_test_idx, axis=0, inplace=True)

train_df.reset_index(drop=True, inplace=True)  # 인덱스 초기화
test_df.reset_index(drop=True, inplace=True)   # 인덱스 초기화

print("========= 삭제 완료 검증 수행 ===========")
for idx, sequence in enumerate(train_df['sequence']):
    if(len(sequence) < 1):
        print(idx, sequence)

print(train_df[25:30])
print(test_df[57:62])

# 타깃 라벨 추출
y_train = np.array(train_df['label'])
y_test = np.array(test_df['label'])

print(len(train_df['sequence']))   # 최종 훈련데이터 31901 개 샘플
print(len(y_train))                     # 최종 훈련데이터 라벨 31901 개
print(len(test_df['sequence']))    # 최종 테스트데이터 31554 개 샘플
print(len(y_test))                      # 최종 테스트데이터 라벨 31554 개

train_review_sequences_len = [len(sequence) for sequence in  train_df['sequence']]
train_review_sequences_arr = np.array(train_review_sequences_len)
print('max : ', np.max(train_review_sequences_arr))  # 훈련 리뷰데이터 최대 길이 63
print('mean : ', np.mean(train_review_sequences_arr)) # 평균 길이 10.734114918027648
#
# # import matplotlib.pyplot as plt
# # plt.hist(train_review_sequences_len, bins=50)
# # plt.show() # pad 적용 30 길이로 동일하게 맞추자
#
X_train_pades = pad_sequences(train_df['sequence'], maxlen=30)
X_test_pades = pad_sequences(test_df['sequence'], maxlen=30)

print(len(X_train_pades[0]))
print(X_train_pades[:1])
print(len(X_test_pades[0]))
print(X_test_pades[:1])