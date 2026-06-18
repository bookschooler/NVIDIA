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

tokenizer.fit_on_texts(train_df['document'])

#################################################################################################################

from tensorflow.keras.models import load_model
best_model = load_model('movie_review_bestmodel.keras') # 앞서 저장한 모델 로드

# 새로운 리뷰 데이터 예측
from konlpy.tag import Okt
import os
import re

# 한국어 토근화 및 패딩처리 위해 Okt클래스 추가
# os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17.0.2\bin'
okt = Okt() # KoNLPy 제공 형태소 분석기

from tensorflow.keras.preprocessing.sequence import pad_sequences

# 조사위주의한국어불용어제거리스트
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

def new_review_predict(review_string):

    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]','', review_string) # 한국어와 공백 이외의 내용 삭제
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    print(new_sentence) # ['영화', '굿', '잼']
    # [new_sentence] : 불용어 처리된 단어 리스트를 정수 인코딩 sequences 데이터 형성을
    # 위해하나로묶어서([]) 변환해줘야함
    encoded = tokenizer.texts_to_sequences( [new_sentence] ) # 정수 인코딩
    print(encoded) # [[1, 363, 334]]
    sentence_padding = pad_sequences(encoded, maxlen = 30) # 패딩 적용 동일 길이 Sequences 형성
    print(sentence_padding)
    #[[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    # 0   0  0   0  0  0   0  0  0  1363 334]]
    score = float(best_model.predict(sentence_padding) ) # new_sentence 예측
    if(score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))

new_review_predict('이 영화 굿 잼')
new_review_predict('이렇게 재미없는 영화는 처음')
new_review_predict('뭐 이런 영화가 다 있어')
new_review_predict('에잇 돈 날렸네')
new_review_predict('이 영화 꼭 추천 도장 꽉!')