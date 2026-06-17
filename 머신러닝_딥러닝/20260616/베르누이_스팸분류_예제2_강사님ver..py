# 강사님 ver.

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

df = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260616/spam.csv')
df = df[:].copy()
print(df)

import re
def aaa(s):
    return re.sub(r'[^a-zA-Z\s]', '', s)
df['Message'] = df['Message'].apply(aaa)
df['Category'] = df['Category'].map({'ham':0, 'spam':1})
print(df)

x = df['Message']
y = df['Category']

cv = CountVectorizer(binary=True)
x_cv = cv.fit_transform(x)
x_encoded = x_cv.toarray()
print(len(cv.get_feature_names_out()))

# 학습
bnb = BernoulliNB()
y = y.astype('int')
bnb.fit(x_encoded, y)
print(bnb.score(x_encoded, y))
#print(bnb.score(x_encoded, y))

############

temp = cv.transform(['last discount event of today'])
print(temp.toarray())
pred = bnb.predict(temp)
print(pred)

# 새로운 이메일 데이터 하나 추가 예측

