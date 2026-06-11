import numpy as np
import pandas as pd

# 데이터셋 불러와서 대충 확인하기
scidf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260609/HeartDiseaseTrain-Test.csv')
print(scidf)
print(scidf.info())
print(scidf.head())


# 데이터 전처리 및 라벨링 작업
scidf['sex'] = scidf['sex'].map({'Male':0, 'Female':1})
scidf['chest_pain_type'] = scidf['chest_pain_type'].map({'Typical angina':1, 'Atypical angina':2, 
                                                         'Non-anginal pain':3, 'Asymptomatic':4 })
scidf['fasting_blood_sugar'] = scidf['fasting_blood_sugar'].map({'Lower than 120 mg/ml':0, 'Greater than 120 mg/ml':1})
scidf['rest_ecg'] = scidf['rest_ecg'].map({'Normal':0, 'ST-T wave abnormality':1, 'Left ventricular hypertrophy':2})
scidf['exercise_induced_angina'] = scidf['exercise_induced_angina'].map({'No':1, 'Yes':1})
scidf['slope'] = scidf['slope'].map({'Upsloping':1, 'Flat':2, 'Downsloping':3})
scidf['vessels_colored_by_flourosopy'] = scidf['vessels_colored_by_flourosopy'].map({'Zero':0, 'One':1,
                                                                                     'Two': 2, 'Three':3, 'Four':4})
scidf['thalassemia'] = scidf['thalassemia'].map({'No':0, 'Normal':3, 'Fixed Defect':6, 'Reversable Defect':7})
print(scidf.head())
print(scidf.info())
print(scidf.shape)

# 결측치 확인하기 
print(scidf.isnull().sum())
print(scidf.isnull().sum(axis=1))

# X축과 Y축 정해주기
scidf_x = scidf.iloc[:, :-1]
scidf_y = scidf.iloc[:, -1]

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = \
    train_test_split(scidf_x, scidf_y, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Scaler로 정규화   
train_scaled = scaler.fit_transform(train_x) 
test_scaled = scaler.transform(test_x) #test는 transform만 해야함.


# 모델 생성  및 평가
# 로지스틱 회귀 ( 분류 ) 모델 준비

from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression() # 모델 준비 완료

# 모델 학습
lr_model.fit(train_scaled, train_y)
#==> 최적의 가중치(w), 편향(b)을 갖는 모델이 완성


# 모델 성능 평가
print('test acc : ', lr_model.score(test_scaled, test_y))
print('train acc : ', lr_model.score(train_scaled, train_y))

# 가중치(w) , 절편(b)
# : conf_  , intercept_
print( lr_model.coef_ , lr_model.intercept_)

# 모델 예측 추정치
print( lr_model.predict(test_scaled[:5] ) )

# Z값으로 변환
decisions = lr_model.decision_function( test_scaled[:5])
print(decisions)

from scipy.special import expit
print( expit(decisions) )
my_proba = lr_model.predict_proba(decisions)
