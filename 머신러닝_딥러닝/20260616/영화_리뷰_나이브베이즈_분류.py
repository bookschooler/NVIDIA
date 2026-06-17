import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf, precision=8, suppress=True)

# 데이터셋 불러오기
mvdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260616/IMDB Dataset.csv')
mvdf.info()
# mvdf = mvdf[:200].copy()
print(mvdf)

# review에서 영어만 골라내기
import re
def aaa(s):
    return re.sub(r'[^a-zA-Z\s]', '', s)
mvdf['review'] = mvdf['review'].apply(aaa)
mvdf['sentiment'] = mvdf['sentiment'].map({ 'positive':1, 'negative':0 })
print(mvdf)

# x, y 분류
train_x = mvdf['review']
train_y = mvdf['sentiment']

# 라벨 변경하기 
# sentiment 컬럼을 수치 데이터로 변경
mvdf['sentiment'] = mvdf['sentiment'].map({ 'positive':1, 'negative':0 })
print(mvdf)

# X인 리뷰도 Vectorize해주고 toarray해줘서 배열로 변환(전처리)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()  # 여기에선 binary를 주면 
train_cv = cv.fit_transform(train_x)
# train_cv_encoded = train_cv.toarray()
# print(train_cv_encoded)
# print(len(cv.get_feature_names_out()))
# print(cv.get_feature_names_out())


# MultiNaiveBayes 모델 준비
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()   # 다항분포 나이브베이즈

# 모델 학습
mnb.fit(train_cv, train_y)
print('acc: ', mnb.score(train_cv,train_y))

# 새로운 영화 리뷰 데이터 입력해서 예측해보기

# 1. 원본 데이터셋을 메모리에 깨끗하게 새로 올립니다.
mvdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260616/IMDB Dataset.csv')

# 2. 텍스트 정제
def aaa(s):
    return re.sub(r'[^a-zA-Z\s]', '', s)
mvdf['review'] = mvdf['review'].apply(aaa)

# 3. [중요] 딱 한 번만 숫자로 변경합니다. (이후 다시 실행 금지)
mvdf['sentiment'] = mvdf['sentiment'].map({ 'positive': 1, 'negative': 0 })

# 4. 전체 학습 데이터 설정
new_x = mvdf['review'][100:200]
new_y = mvdf['sentiment'][100:200]

new_x_cv = cv.transform(new_x)

pred = mnb.predict(new_x_cv)

new_score = mnb.score(new_x_cv, new_y)
print(mnb.score(new_x_cv, new_y))

for review, prob in zip(new_x, positive_probs):
    if prob >= 0.5:
        # [순서 5] 리뷰의 앞부분 50글자와 함께 "positive"라는 글자, 그리고 실제 확률을 화면에 출력합니다.
        print(f"리뷰: {review[:50]}... -> [positive] (확률: {prob:.4f})")
    # [순서 6] 확률이 0.5 미만인 나머지 모든 경우라면 아래 문장을 수행합니다.
    else:
        # [순서 7] 리뷰의 앞부분 50글자와 함께 "negative"라는 글자, 그리고 실제 확률을 화면에 출력합니다.
        print(f"리뷰: {review[:50]}... -> [negative] (확률: {prob:.4f})")






