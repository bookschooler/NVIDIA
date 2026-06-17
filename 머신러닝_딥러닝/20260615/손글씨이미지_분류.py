from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# 데이터셋 불러오기
mnist = datasets.load_digits()  # 손글씨 이미지 데이터셋

# 데이터 모양 파악
print(mnist.data.shape)

features = mnist['data']
print(len(features[0]))
print(len(features))

labels = mnist['target']
print(np.unique(labels, return_counts=True))

# 시각화로 무슨 이미지인지 확인
# print(features[8].reshape(8,8))
# plt.imshow(features[8].reshape(8,8), cmap='gray')
# plt.savefig('mnist_handwriting.jpeg')

print(features.shape)   # (1797, 8, 8, 1) => (batch_size, h_img, v_img, channel)

# 차원 맞춰주고 (=Shape 바꿔주고) , 정규화까지 (Scale 조정)
features = features.reshape(-1, 8, 8, 1) / 255.0
print(features[0])

# features와 label을 train / test로 분할 ( 분할 비율은 0.2로 )
from sklearn.model_selection import train_test_split
train_x, val_x, train_y, val_y = train_test_split(features, labels, test_size= 0.2, random_state=42)
print(len(train_x))
print(len(val_x))

# y를 category => One-Hot Encoding 해줘야 함
from tensorflow.keras.utils import to_categorical  
train_y = to_categorical(train_y, num_classes = 10)  
val_y = to_categorical(val_y, num_classes = 10)
print(val_y.shape)
# 데이터 전처리 및 데이터 준비 완료

# 모델 준비 => 이미지를 분류하는 모델 설계 ( 10개 클래스를 분류 => 다중 분류)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

# 뼈대 설계
model = Sequential()

# CNN 부분 설계
model.add( Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same', input_shape = (8,8,1) )) 
model.add ( MaxPooling2D(2,2))
model.add( Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same' )) 
model.add ( MaxPooling2D(2,2))
model.add ( Flatten())
model.summary()

# FC Layer 설계
model.add (Dense ( units = 50, activation='relu') )
model.add( Dropout(0.4) )
model.add( Dense( 30, activation='relu'))
model.add( Dense( 10, activation='softmax'))
model.summary()

# 학습 전 Compile 설정
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# Callback 기능 설정
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint

modelpath = './handwriting_bestmodel.keras'
checkpoint_cb = ModelCheckpoint(filepath = modelpath, monitor='val_loss', save_best_only=True)
earlystop_cb = EarlyStopping(monitor='val_loss', patience = 3, restore_best_weights = True )

# 모델 학습(Fit)
# 정답을 정수 형태로 그대로 사용할 거면 => sparse categorical crossentropy
# 정답을 원한 인코딩 형태로 반환할거면 => categorical_crossentropy
model.fit(train_x, train_y, batch_size=4, epochs = 100, validation_data = (val_x, val_y),callbacks = (checkpoint_cb, earlystop_cb), verbose=1 )


# 이미지 분류에 특화된 모델 => cnn
# 2개의 Conv + 2개의 Pooling Layer 
# Flatten +  Dropout + FC layer 추가
# 출력층 => 10개의 뉴런 설정
# 손실함수 => categorical_crossentropy
# 모델 설계 후 모델 학습



