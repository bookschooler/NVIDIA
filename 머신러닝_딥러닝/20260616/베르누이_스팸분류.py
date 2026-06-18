import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer # 메일 제목을 vectorize해줌 
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

pd.set_option('display.max_rows', None)


# 데이터셋 준비
email_list = [
    {'email title': 'free game only today', 'spam': True},
    {'email title': 'cheapest flight deal', 'spam': True},
    {'email title': 'limitd time offer only today only today', 'spam': True},
    {'email title': 'today meeting schedule', 'spam': False},
    {'email title': 'your flight schedule attached', 'spam': False},
    {'email title': 'your credit card statement', 'spam': False},
]

# 데이터 프레임으로 변환
emaildf = pd.DataFrame(email_list)
print(emaildf)

# 분류를 위해 label을 수치로 변환
emaildf['spam'] = emaildf['spam'].map( {True:1, False:0} )
print(emaildf)

train_x = emaildf['email title']
train_y = emaildf['spam']

cv = CountVectorizer(binary=True)
train_x_cv = cv.fit_transform(train_x)
print(train_x_cv)
print(type(train_x_cv))
train_encoded = train_x_cv.toarray()    # ⭐toarray
print(train_encoded)
print(cv.get_feature_names_out())

# 모델 만들기
bnb_model = BernoulliNB()
print(type(train_y))
print(train_y)
train_y = train_y.astype('int')

# 학습
print(type(train_encoded))
bnb_model.fit(train_encoded, train_y)

print('acc :', bnb_model.score(train_encoded, train_y))

# 임의의 메일 제목 만들어서 예측해보기

temp_email_cv = cv.transform(['last discount event of today',
                            'the payment document is attached and sent',
                            'company collaboration event free ofer'])

print(temp_email_cv)
temp_email_encoded = temp_email_cv.toarray()

pred1 = bnb_model.predict(temp_email_encoded)
print(pred1)


# 캐글 데이터에서 100개만 꺼내가지고 정규표현식으로 영어만 필터링하기
spam_dataset = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260616/spam.csv')
spamdf = spam_dataset[:100].copy()
print(spamdf.head(3))

# 정규표현식 써서 message에서 영어만 골라내기 
import re

spamdf['Message'] = spamdf['Message'].apply(
    lambda x: re.sub(r'[^a-zA-Z\s]', '', str(x)))
print(spamdf['Message'])


# Message를 CountVectorize해서 전처리 해주기
kaggle_x_encoded = cv.transform(spamdf['Message']).toarray()

# 이 새로운 데이터로 예측하기
pred2 = bnb_model.predict(kaggle_x_encoded)
print(pred2)

# 성능 평가하기
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

kaggle_y = spamdf['Category'][:100].map({
    'ham':0,
    'spam':1 } )

print(f'성능평가 :', bnb_model.score(kaggle_x_encoded, kaggle_y))
print(spamdf['Category'].value_counts())
print(confusion_matrix(kaggle_y, pred2))

# re 강사님 ver.
# import re
# def EmailMessageControl(arg):
#     re.sub(r'[^a-zA-Z\s]', '', arg)
# spamdf['Message'] = spamdf['Message'].apply(EmailMessageControl)

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import BernoulliNB

# cv= CountVectorizer()
# train_x = cv.fit_transform(spamdf['Message']).toarray()

# print(len( cv.get_feature_names_out()))