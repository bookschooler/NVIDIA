import numpy as np
import pandas as pd

# 1. 데이터셋 불러오기
winedf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260611/wine_dataset.csv')

# 2. 데이터셋 확인
print(winedf.shape)
print(winedf.info())
print(winedf.head(5))

print(winedf.isnull().sum())

# 3. y값 red:1, white: 0으로 매핑 => X, Y로 나누기

winedf['style'] = winedf['style'].map({'white':0, 'red':1})

x = winedf.iloc[:, :-1]
y = winedf.iloc[:, -1]

# 4. train/ test 세트로 분리 후 확인
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
print(train_x[:5])

# 5. 학습 전 feature들 scaler로 표준화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_x)
test_scaled = scaler.transform(test_x)

print("train scaled: ")
print(train_scaled[:10])

# 6. 모델 설계
# # 입력 특성 데이터 12개 -> 뉴런 무조건 12개 이상  
# 6497행 13개 특성 
# batch_size = 4?
# epochs = 200

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import metrics

# 7. 모델 뼈대 만들기
model  = Sequential()

# 8. 입력층/은닉층/출력층 만들기
model.add( Dense(units = 24, input_dim = 12, activation = 'leaky_relu'))
model.add( Dense(units = 36, activation = 'leaky_relu'))
model.add( Dense(units = 1, activation = 'sigmoid'))

model.summary()

# 9. fit 전 모델에 환경설정 
model.compile(loss = 'binary_crossentropy' , optimizer = 'adam', metrics = ['accuracy', 'precision', 'recall', 'AUC'])

# 10. 학습(Fit)
model.fit(train_scaled, train_y, batch_size =30, epochs = 100, verbose = 1)

# 11. test 세트로 예측해보기
model.predict(test_scaled)

# 12. 성능 측정(evaluate)
model.evaluate(test_scaled, test_y)

# 13. 저장
model.save('wine_bestmodel.keras')

import pickle

pickle.dump(
    scaler,
    open("wine_bestmodel.pkl", 'wb')
)
