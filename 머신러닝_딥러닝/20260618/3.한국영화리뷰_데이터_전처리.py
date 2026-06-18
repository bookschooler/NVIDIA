import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 50)




review_df= pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260618/ratings_train.csv',
                       header = 0, delimiter = '\t', quoting=3)  #⭐
print(review_df)
print(review_df.info()) # 결측치가 있네 ... ? 

# 결측치 제거
review_df.dropna(how='any', inplace = True) #⭐ how용법 찾기 
# how = 'any' 해당 줄(행)에 빈칸(NaN)이 단 하나라도(any) 있다면, 그 줄은 통째로 쓰레기통에 버려!
# how = 'all' 해당 줄(행)의 모든 칸이(all) 전부 다 빈칸(NaN)일 때만 쓰레기통에 버려!
print(review_df.info())  
print(review_df.head(5))

# 라벨 (타겟) 컬럼데이터의 type을 실수에서 정수로 변환해줘야함
review_df['label'] = review_df['label'].astype('int64')
print(review_df.info())  
print(review_df.head(5))

# 리뷰 데이터의 항목 중 중복 데이터가 있으면 찾아서 제거
print(review_df['document'].nunique())  #nunique 고유값의 개수를 반환 
review_df.drop_duplicates(subset='document', inplace = True)    # subset = 컬럼명
print(review_df.info())     
# 결측치, 중복 제거 후 총 데이터 수 => 32163 개

# ## 한글과 공백을 제외한 모든 문자를 제거 ###
# 원래대로라면 ⭐apply함수로 일괄적으로 적용해야하는데 문자열 속성의 함수인 str.replace를 써보자! 
import re
# review_df['document'] = review_df['document'].str.replace(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]', '') # ㄱ-힣\s 이것도 같은 뜻 !⭐
# review_df['document'] = review_df['document'].apply(lambda x: re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', str(x))) ⭐

# ⭐이 함 수 부분 이해하기 
def ReviewFiltering(arg):
    return re.sub(r'[^ㄱ-힣\s]','',arg)

review_df['document'] = review_df['document'].apply(ReviewFiltering)
review_df['document'] = review_df['document'].str.replace('^\s+','')

print(review_df.sample(100))
print(review_df.info())

# def Multispace(arg):
#     return re.sub(r'^\s+', '', arg)

# review_df['document'] = review_df['document'].apply(Multispace)

# def Nullreplace(arg):                                             ⭐ 텍스트 정제 하는 과정 나중에 더 공부하기! 
#     return re.sub(r' ', np.nan, arg)                          이것 저것 시도해봤지만 실패 ... 

# review_df['document'] = review_df['document'].apply(Nullreplace)
# print(review_df.info())


# test 데이터 역시 전처리 해주기

# 전처리 된 train / test 리뷰 불용어 제거해주기

from konlpy.tag import Okt
from tqdm import tqdm   # 처리 상태를 막대바로 표현해줌

okt = Okt()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다', '줄', ]

X_train = []
for sentence in tqdm(review_df['document']):
    tokenized_sentence = okt.morphs(sentence, stem=True) # 각 문장을 토큰화
    sentence_removed_stopwords = \
    [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    #불용어 제거된 단어 리스트를 한문장으로 합친 다음 X_trainlist에 추가
    X_train.append(' '.join(sentence_removed_stopwords))

# print(review_df[:5])
# print('='*80)
# print(X_train[:5]) # 불용어가 제거된 문장 모음 리스트

review_df['document'] = X_train
print(review_df)

