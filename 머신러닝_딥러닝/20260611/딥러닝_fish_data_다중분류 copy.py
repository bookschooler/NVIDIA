import numpy as np
import pandas as pd


# e 지수 표현하는 과학적 표기 대신 소수점 이하 8자리까지 표현해라~   
# e의 몇승 이렇게 표시하는 걸 과학적 표기라 함

# 1. 넘파이 출력 설정 (소수점 8자리, 과학적 표기법 끄기)
np.set_printoptions(precision=8, suppress=True)
np.set_printoptions(threshold=np.inf) # ... 으로 줄이지 않고 무한 출력! 

# 💡 2. 판다스 출력 설정 (에러 나던 문법을 지우고 올바른 짝으로 교체!)
pd.set_option('display.max_rows', None)     # 행을 제한 없이 다 출력
pd.set_option('display.max_columns', None)  # 열을 제한 없이 다 출력
pd.set_option('display.width', 1000)        # 가로 폭을 넉넉하게 넓히기
fishdf = pd.read_csv('/home/sophie/tf_env/머신러닝_딥러닝/20260611/fish_data1.csv')

print(fishdf)
print(fishdf.info())
print(fishdf.shape)
print(fishdf['Species'].unique())



print(fishdf.isnull().sum())
print(fishdf.isnull().sum(axis=1))

#Series 를 넘파이 배열로 변환해주는 메서드 ==> to_numpy()
fish_target = fishdf['Species'].to_numpy()
print(fish_target)
print(fishdf.columns)
fish_train = fishdf[ ['Weight', 'Length', 'Diagonal', 'Height', 'Width'] ].to_numpy()
print(fish_train)

# 문자열을 수치 형태로 변환 ( Labelencoder 사용)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

y_encoded = le.fit_transform(fish_target)
print(y_encoded)
print(le.classes_)

# categorical_crossentropy()  ==> 정답이 one-hot encoding 상태여야함.
from tensorflow.keras.utils import to_categorical
y_onehot = to_categorical(y_encoded)
print(y_onehot)

# train / test 데이터 분리
from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = \
    train_test_split(fish_train, y_onehot, random_state=42)

print(train_x.shape)
print(val_x.shape)

# 특성 데이터에 대한 스케일 조정 (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train_scaled = scaler.fit_transform(train_x)
test_scaled = scaler.transform(val_x)

# scaler 함수 저장해주기
import joblib
joblib.dump(scaler, 'fish_scaler.pkl' )

# # scaler 읽어들일 땐
# joblib.load('fish_scaler.pkl')

# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import metrics

multi_model = Sequential()
multi_model.add( Dense( units = 10, input_dim= 5 , activation = 'leaky_relu' ))    
multi_model.add( Dense( units = 7, activation = 'softmax' ))    # 다중분류의 출력층의 뉴런 개수는 분류하고자 하는 종류의 개수

# 뼈대에 환경설정 해주기
multi_model.compile( loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# val 데이터를 가지고 loss 개선됐을 때만 그 조건을 저장하고 Early Stop해주는 기능 추가 => earlystopping, modelcheckpoint 사용
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping

checkpoint_cb = ModelCheckpoint(filepath = './fish_bestmodel.keras', monitor='val_loss', verbose=1, save_best_only=True)
earlystop_cb = EarlyStopping( monitor = 'val_loss', patience = 5, restore_best_weights=True)


# 모델 학습(Fit)
history = multi_model.fit(train_scaled, train_y, validation_data = (test_scaled, val_y), batch_size = 1, epochs = 500, verbose = 1, 
                callbacks = [checkpoint_cb, earlystop_cb])

# => 여기서 모델이 알아서 제일 best 버전으로 저장됨

# val_loss, train_loss 뽑아서 시각화 해보기
val_loss = history.history['val_loss']
train_loss = history.history['loss']

import matplotlib.pyplot as plt

plt.plot(val_loss, c='red')
plt.plot(train_loss, c='blue')

plt.savefig('딥러닝_fish_다중분류_그래프.jpeg')



# # 모델 성능평가
# print('Test acc: ' , multi_model.evaluate(test_scaled, test_y)[1])

# multi_model.save('fish_multi_classify.keras')



