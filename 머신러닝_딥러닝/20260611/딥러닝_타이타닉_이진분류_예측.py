# # 학습된 모델 불러오기
# from tensorflow.keras.models import load_model

# titanic_bestmodel = load_model('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_best_model.keras')
# titanic_bestmodel.summary()

# # 머신러닝처럼 새로운 3 사람의 정보를 만들어서 생존여부 예측하기
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# from sklearn.linear_model import LogisticRegression
# lr_model = LogisticRegression() # 모델 준비 완료


# titanicdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_passengers.csv')

# # X_train = titanicdf[['gender', 'Age', 'Class_1', 'Class_2']]


# print(titanicdf)
# print(titanicdf.info())
# print(titanicdf.head())

# new_data = {
#     'gender': [0, 1, 1, 1],           # 0: 남성, 1: 여성
#     'Age': [25, 33, 18, 4],
#     'Class_1': [1, 1, 1, 1],          # 모두 1등급
#     'Class_2': [0, 0, 0, 0]
# }

# my_df = pd.DataFrame(new_data, index=['홍길동', '짜오잉', '잔다르크', '티니핑'])

# my_scaled = scaler.fit(new_data)

# my_predict = titanic_bestmodel.predict( my_scaled )
# my_proba = titanic_bestmodel.predict_proba(my_scaled)

# print(my_predict)
# print(my_proba)

import numpy as np  # 1  # 넘파이 라이브러리를 불러옵니다.
import pandas as pd  # 2  # 판다스 라이브러리를 불러옵니다.
from sklearn.preprocessing import StandardScaler  # 3  # 데이터 표준화를 위한 StandardScaler를 불러옵니다.
from tensorflow.keras.models import load_model  # 4  # 텐서플로우에서 저장된 모델을 불러오는 함수를 로드합니다.

# 1. 학습된 딥러닝 모델 로드
titanic_bestmodel = load_model('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_best_model.keras')  # 5  # 지정된 경로에서 케라스 모델을 불러옵니다.

# 2. 원본 데이터 로드 및 예측 데이터와 동일한 구조로 전처리
titanicdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_passengers.csv')  # 6  # 원본 타이타닉 CSV 파일을 데이터프레임으로 읽어옵니다.

# [전처리 1] gender 열의 문자열(male, female)을 숫자(0, 1)로 변환
titanicdf['gender'] = titanicdf['gender'].replace({'male': 0, 'female': 1})  # 7  # 문자열을 새 데이터 구조와 맞춰 숫자로 치환합니다.

titanicdf['Class_1'] = np.where(titanicdf['Pclass'] == 1, 1, 0)  # 9  # 1등급이면 1, 아니면 0
titanicdf['Class_2'] = np.where(titanicdf['Pclass'] == 2, 1, 0)

# [전처리 2] Pclass 열을 원-핫 인코딩하여 Class_1, Class_2 열 생성
titanicdf = pd.get_dummies(titanicdf, columns=['Pclass'], drop_first=True, dtype=int)  # 8  # Pclass 열을 원-핫 인코딩하여 데이터프레임에 결합하고 원본 열은 삭제합니다.

# [전처리 3] 결측치(NaN) 처리 - Age 열의 빈칸을 평균값으로 채우기
titanicdf['Age'] = titanicdf['Age'].fillna(titanicdf['Age'].mean())  # 10  # 결측치가 있으면 스케일러가 에러를 내므로 평균값으로 채웁니다.

# 학습에 사용될 독립변수 데이터셋 구성 (새로운 데이터와 컬럼 순서/개수 완벽 일치)
X_train = titanicdf[['gender', 'Age', 'Class_1', 'Class_2']]  # 11  # 모델이 학습했던 4개의 특성만 순서대로 추출합니다.

# 3. 스케일러 정의 및 원본 데이터 기준 학습(fit)
scaler = StandardScaler()  # 12  # 표준화 스케일러 객체를 생성합니다.
scaler.fit(X_train)  # 13  # 딕셔너리가 아닌, 올바른 데이터프레임(X_train)으로 스케일러 기준을 학습시킵니다.

# 4. 예측할 새로운 데이터 정의 및 변환(transform)
new_data = {  # 14  # 새로운 예측 데이터를 딕셔너리로 정의하기 시작합니다.
    'gender': [0, 1, 1, 1],  # 15  # gender 리스트를 지정합니다.
    'Age': [25, 33, 18, 4],  # 16  # Age 리스트를 지정합니다.
    'Class_1': [1, 1, 1, 1],  # 17  # Class_1 리스트를 지정합니다.
    'Class_2': [0, 0, 0, 0]  # 18  # Class_2 리스트를 지정합니다.
}  # 19  # 딕셔너리 정의를 마칩니다.

my_df = pd.DataFrame(new_data, index=['홍길동', '짜오잉', '잔다르크', '티니핑'])  # 20  # 딕셔너리를 데이터프레임 구조로 변환합니다.

# [수정 포인트] 학습된 스케일러(scaler)를 사용하여 새로운 데이터프레임(my_df)을 변환합니다.
my_scaled = scaler.transform(my_df.to_numpy())  # 21  # transform 메서드에 변환 대상 데이터프레임을 전달합니다.

# 5. 딥러닝 모델 예측 진행
my_predict = titanic_bestmodel.predict(my_scaled)  # 22  # 표준화된 데이터를 딥러닝 모델에 입력하여 예측값을 얻습니다.

import pickle

pickle.dump( scaler, open("titanic_Scaler.pkl", "wb") )

# print(my_predict)  # 23  # 최종 예측 결과를 터미널 창에 출력합니다.