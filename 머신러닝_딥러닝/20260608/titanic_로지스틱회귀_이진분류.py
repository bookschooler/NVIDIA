# import numpy as np
# import pandas as pd
# pd.set_option('display.max_rows',20)
# pd.set_option('display.max_columns',500)
# import pickle 

# titanicdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260608/titanic_passengers.csv')

# # "titanic_Scaler.pkl" 파일을 바이너리 읽기(rb) 모드로 열어서 스케일러 복원하기
# with open("titanic_Scaler.pkl", "rb") as p:  # 5  # 복원용 보관함 문을 열고 f라는 별명을 붙입니다.
#     loaded_scaler = pickle.load(p)  # 6  # 파일 안의 0과 1 데이터를 파이썬 스케일러 객체로 해동하여 loaded_scaler에 저장합니다.

# print(titanicdf)
# # Survived 컬럼데이터를 타깃으로 활용( 0, 1)
# # 머신러닝 sklearn 은 타깃이 문자열 이어도 성능평가 가능
# # Survived 컬럼열 데이터를 변경
# # 0 ==> fail,  1 ==> suvival
# print(titanicdf.info())
# titanicdf['Survived'] = titanicdf['Survived'].map({1:'suvival',0:'fail'})
# print(titanicdf.head())

# # 모델 입력 데이터 준비
# # gender, Age, Pclass 3가지 컬럼 데이터가 생존/비생존에 많은 영향을 미침
# print(titanicdf['gender'])
# # 'male'(남성)을 0 으로  , 'female'(여성)을 1  로 변경
# titanicdf['gender'] = titanicdf['gender'].map({'male':0, 'female':1})

# # age 컬럼에 np.NaN 결측치가 존재 ==> 결측치 제거 필용
# titanicdf.dropna(subset='Age', inplace=True)
# print(titanicdf.head())
# print(titanicdf.info())

# # age 컬럼에 결측치를 평균데이터로 채워서 사용
# # titanicdf['Age'].fillna(value=titanicdf['Age'].mean(), inplace=True)
# # print(titanicdf.head())
# # print(titanicdf.info())
# print(titanicdf['Pclass'])  #  1 등석과 2등석 데이터만  추출

# # 판다스에 원핫인코딩으로 변환해주는 메서드 ==> get_dummies()
# # 원핫인코딩 ==> 모든 수치 데이터를 0 과 1 로만 표현
# # 1 ==> 001 , 2 ===> 010 ,  3 ==> 100
# onehot_pclass = pd.get_dummies( titanicdf['Pclass'] , prefix='Class', dtype=int)
# print(onehot_pclass)

# # axis=1 ==> 열축으로 두 Dataframe 을 병합해라
# titanicdf = pd.concat([titanicdf, onehot_pclass], axis=1)
# print(titanicdf)

# # Age, gender, Class_1, Class_2  이 4개 컬럼 데이터를 모델 입력 데이터로 사용
# # 'Survived' 컬럼은 모델 정답(target) 데이터로 사용
# titanicdf_x = titanicdf[['gender','Age','Class_1','Class_2']]
# print(titanicdf_x)

# titanicdf_y = titanicdf['Survived']
# print(titanicdf_y)


# # train / test 분리 해서 사용
# from sklearn.model_selection import train_test_split

# train_x, test_x, train_y, test_y = \
#     train_test_split(titanicdf_x, titanicdf_y, random_state=42)

# print(train_x[:10])

# # 특성데이터의 스케일 변환(정규화) ==> 표준점수 정규화 ( 각특성 - 평균 / 표준편차 )
# # from sklearn.preprocessing import StandardScaler
# # scaler = StandardScaler()

# train_scaled = loaded_scaler.fit_transform(train_x) # train 데이터를 정규화 하는 방법을 학습하고 학습이 끝나면
# # 변환 작업을 수행 
# # test데이터셋은 transform() 만 해서 적용만 해야 함
# test_scaled = loaded_scaler.transform(test_x)
# print(train_scaled[:10])

# # 모델 생성  및 평가
# # 로지스틱 회귀 ( 분류 ) 모델 준비
# from sklearn.linear_model import LogisticRegression

# lr_model = LogisticRegression() # 모델 준비 완료

# # 모델 학습
# lr_model.fit(train_scaled, train_y)
# #==> 최적의 가중치(w), 편향(b)을 갖는 모델이 완성

# # 모델 성능 평가
# print('test acc : ', lr_model.score(test_scaled, test_y))
# print('train acc : ', lr_model.score(train_scaled, train_y))

# # 가중치(w) , 절편(b)
# # : conf_  , intercept_
# print( lr_model.coef_ , lr_model.intercept_)

# # 모델 예측 추정치
# print( lr_model.predict(test_scaled[:5] ) )

# # z 값 계산
# decisions = lr_model.decision_function( test_scaled[:5] )
# print(decisions)

# from scipy.special import expit
# print( expit(decisions) )

# # ===== 새로운 데이터 예측 =====
# print('\n' + '='*50)
# print('새로운 데이터 생존 여부 예측')
# print('='*50)

# # 새로운 데이터 생성 (성별, 나이, Class_1, Class_2)
# # 모두 1등급(Pclass=1) 승객이라고 가정 => Class_1=1, Class_2=0
# new_data = {
#     'gender': [0, 1, 1, 1],           # 0: 남성, 1: 여성
#     'Age': [25, 33, 18, 4],
#     'Class_1': [1, 1, 1, 1],          # 모두 1등급
#     'Class_2': [0, 0, 0, 0]
# }

# new_df = pd.DataFrame(new_data, index=['홍길동', '본인', '잔다르크', '티니핑'])
# print('\n입력 데이터:')
# print(new_df)

# # 같은 scaler로 정규화
# new_scaled = loaded_scaler.transform(new_df)

# # 예측
# predictions = lr_model.predict(new_scaled)
# probabilities = lr_model.predict_proba(new_scaled)

# print('\n예측 결과:')
# result_df = pd.DataFrame({
#     '이름': ['홍길동', '본인', '잔다르크', '티니핑'],
#     '생존 예측': ['생존' if p == 'suvival' else '사망' for p in predictions],
#     '생존 확률': [f'{prob[1]:.2%}' for prob in probabilities]
# })
# print(result_df)

# # 상세 정보
# print('\n상세 정보:')
# for i, name in enumerate(['홍길동', '본인', '잔다르크', '티니핑']):
#     print(f'{name}: {predictions[i]} (생존 확률: {probabilities[i][1]:.4f})')

# # lr_model 을 이용해서 새로운 데이터의 생존 여부를 체크

#             # 성별    나이    클래스1     클래스2

# # 홍길동        0      25  
# # 본인          1      33
# # 잔다르크      1       18
# # 티니핑        1       4

# # 위 네 사람의 정보를 DataFrame으로 구성하고 예측해서 생존 여부를 파악해주세요

# my_data = {
#     'gender': [0, 1, 1, 1],           
#     'Age': [25, 33, 18, 4],
#     'Class_1': [1, 1, 1, 1],          
#     'Class_2': [0, 0, 0, 0]
# }

# my_df = pd.DataFrame(my_data, index=['홍길동', '짜오잉', '잔다르크', '티니핑'])
# my_scaled = scaler.transform(my_df)
# my_predict = lr_model.predict( my_scaled )
# my_proba = lr_model.predict_proba(my_scaled)


import pickle  # 1  # 피클 라이브러리를 사용하기 위해 불러옵니다.
import pandas as pd  # 2  # 데이터프레임 처리를 위해 판다스를 불러옵니다.
from tensorflow.keras.models import load_model  # 3  # 저장된 딥러닝 모델을 불러오기 위해 로드 함수를 가져옵니다.

# 1. 저장된 딥러닝 모델과 피클 스케일러 불러오기
titanic_bestmodel = load_model('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_best_model.keras')  # 4  # 딥러닝 모델을 로드합니다.

# [핵심] "titanic_Scaler.pkl" 파일을 바이너리 읽기(rb) 모드로 열어서 스케일러 복원하기
load_scaler = pickle.load(
    open("titanic_scaler.pkl", "rb")
)

# 2. 예측할 새로운 데이터 준비 (앞서 완성한 원-핫 인코딩 구조인 Pclass_2, Pclass_3 형태)
new_data = {  # 7  # 예측용 데이터를 딕셔너리로 정의하기 시작합니다.
    'gender': [0, 1, 1, 1],  # 8  # 남성 0, 여성 1
    'Age': [25, 33, 18, 4],  # 9  # 나이 데이터
    'Pclass_1': [0, 0, 0, 0],  # 10  # 2등석 여부 (모두 1등석이므로 0)
    'Pclass_2': [0, 0, 0, 0]   # 11  # 3등석 여부 (모두 1등석이므로 0)
}  # 12  # 딕셔너리 정의를 마칩니다.

my_df = pd.DataFrame(new_data, index=['홍길동', '짜오잉', '잔다르크', '티니핑'])  # 13  # 데이터프레임으로 변환합니다.

# 3. 불러온 스케일러로 데이터 변환 진행 (이미 fit이 완료된 상태이므로 transform만 수행!)
my_scaled = load_scaler.transform(my_df.to_numpy())  # 14  # 데이터프레임을 넘파이 배열로 바꿔 해동된 스케일러로 변환합니다.

# 4. 최종 예측
my_predict = titanic_bestmodel.predict(my_scaled)  # 15  # 변환된 데이터를 모델에 넣어 생존 여부를 예측합니다.
print(my_predict)  # 16  # 예측 결과를 출력합니다.