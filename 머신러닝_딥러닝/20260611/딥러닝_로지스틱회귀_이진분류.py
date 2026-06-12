import numpy as np
import pandas as pd
pd.set_option('display.max_rows',20)
pd.set_option('display.max_columns',500)

titanicdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260611/titanic_passengers.csv')
print(titanicdf)
# Survived 컬럼데이터를 타깃으로 활용( 0, 1)
# 딥러닝에서 타깃데이터 0과 1 그대로 사용
print(titanicdf.info())
# titanicdf['Survived'] = titanicdf['Survived'].map({1:'suvival',0:'fail'})
print(titanicdf.head())

# 모델 입력 데이터 준비
# gender, Age, Pclass 3가지 컬럼 데이터가 생존/비생존에 많은 영향을 미침
print(titanicdf['gender'])
# 'male'(남성)을 0 으로  , 'female'(여성)을 1  로 변경
titanicdf['gender'] = titanicdf['gender'].map({'male':0, 'female':1})

# age 컬럼에 np.NaN 결측치가 존재 ==> 결측치 제거 필용
titanicdf.dropna(subset='Age', inplace=True)
print(titanicdf.head())
print(titanicdf.info())

# age 컬럼에 결측치를 평균데이터로 채워서 사용
# titanicdf['Age'].fillna(value=titanicdf['Age'].mean(), inplace=True)
# print(titanicdf.head())
# print(titanicdf.info())
print(titanicdf['Pclass'])  #  1 등석과 2등석 데이터만  추출

# 판다스에 원핫인코딩으로 변환해주는 메서드 ==> get_dummies()
# 원핫인코딩 ==> 모든 수치 데이터를 0 과 1 로만 표현
# 1 ==> 001 , 2 ===> 010 ,  3 ==> 100
onehot_pclass = pd.get_dummies( titanicdf['Pclass'] , prefix='Class', dtype=int)
print(onehot_pclass)

# axis=1 ==> 열축으로 두 Dataframe 을 병합해라
titanicdf = pd.concat([titanicdf, onehot_pclass], axis=1)
print(titanicdf)

# Age, gender, Class_1, Class_2  이 4개 컬럼 데이터를 모델 입력 데이터로 사용
# 'Survived' 컬럼은 모델 정답(target) 데이터로 사용
titanicdf_x = titanicdf[['gender','Age','Class_1','Class_2']]
print(titanicdf_x)

print("타깃 데이터 체크: ")
titanicdf_y = titanicdf['Survived']
print(titanicdf_y)

titanicdf.info()    # 각 특성데이터 타입 체크

# train / test 분리 해서 사용
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = \
    train_test_split(titanicdf_x, titanicdf_y, random_state=42)

print(train_x[:10])

# 특성데이터의 스케일 변환(정규화) ==> 표준점수 정규화 ( 각특성 - 평균 / 표준편차 )
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train_scaled = scaler.fit_transform(train_x) # train 데이터를 정규화 하는 방법을 학습하고 학습이 끝나면
# 변환 작업을 수행 
# test데이터셋은 transform() 만 해서 적용만 해야 함
test_scaled = scaler.transform(test_x)
print("train scaled: ")
print(train_scaled[:10])

# 입력 특성 데이터 4개 
# batch_size = 16
# epochs = 200
# 딥러닝 모델 설계 => 교재 그림 참조

# 필요한 환경 세팅
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import metrics
import pandas as pd
import numpy as np

# 모델 뼈대 만들기
model = Sequential()

# 입력층 / 은닉층 / 출력층 만들기
model.add(Dense (units = 8, input_dim = 4, activation = 'leaky_relu'))
model.add(Dense (units = 4, activation = 'leaky_relu'))
model.add(Dense (units = 1, activation = 'sigmoid'))

# 모델 구조 잘 만들었나 한 번 확인해주기
model.summary()

# fit하기 전 환경 설정
model.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy', 'Precision', 'Recall', 'AUC'])

# 학습(fit) 시키기
model.fit(train_scaled, train_y, batch_size = 10, epochs = 400, verbose = 1)

# 예측해보기
model.predict(test_scaled)

# 성능 측정하기
print(f'성능측정값: ', model.evaluate(test_scaled, test_y) )

# 모델 설계 후 fit까지만 진행

model.save('titanic_best_model.keras')  # 모델 전체 저장 (모델 구조 및 가중치)
