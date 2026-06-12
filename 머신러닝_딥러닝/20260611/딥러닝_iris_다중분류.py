import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',100)
pd.set_option('display.width',1000)
np.set_printoptions(precision=8, suppress=True)

iris = load_iris()
print(iris)

# 1. 데이터 불러와서 X, Y로 분류하기 
# 타겟 ==> iris['target']
x = iris['data']
y = iris['target']

print(x)
print(y)

# 2. Y를 One-Hot Encoding 해주기
from sklearn.preprocessing import OneHotEncoder
y_reshaped = y.reshape(-1, 1)   # reshape을 해준 이유: 2차원 배열로 만들어주기 위해서
oh_encoder = OneHotEncoder(sparse_output=False)
y_onehot = oh_encoder.fit_transform(y_reshaped)

# 3. train/ test 데이터셋으로 나눠주기 
train_x, test_x, train_y, test_y = train_test_split(x, y_onehot, random_state=42)

# 4. scale조정 해주기
from sklearn.preprocessing import StandardScaler
scaler =  StandardScaler()
train_scaled = scaler.fit_transform(train_x)
test_scaled = scaler.transform(test_x)

# scaler 함수 저장해주기
import joblib
joblib.dump(scaler, 'iris_scaler.pkl' )

# 다중 분류 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import metrics

model = Sequential()
model.add(Dense (units = 8, input_dim = 4, activation = 'leaky_relu'))
model.add(Dense (units = 3,  activation = 'softmax'))

model.summary()

# 뼈대에 환경설정 붙여주기
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# 학습(Fit)
model.fit(train_x, train_y, batch_size = 1, epochs = 100, verbose = 1)

# 성능 평가(evaluate)
print(f'test 데이터셋 acc: ' , model.evaluate(test_x, test_y, verbose=1))
print(f'train 데이터셋 acc: ' , model.evaluate(train_x, train_y, verbose=1))

model.save('iris_classify.keras')


# 'setosa', 'versicolor', 'virginica' 3가지 붓꽃 클래스 분류( 다중분류 )

# scale이랑 모델은 별도 저장하기 
# 단) categorical_crossentropy만 사용
# 예측 