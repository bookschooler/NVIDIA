import numpy as np
from tensorflow.keras.datasets import fashion_mnist

(train_x, train_y), (test_x, test_y) = fashion_mnist.load_data()
print(len(train_x), len(test_x))

# 정답의 클래스 분류와 몇 어떤 클래스가 몇 개 있는지까지 보여줌
print( np.unique(train_y, return_counts = True))    # ⭐return_counts = 클래스별 몇 개 있는지
print( np.unique(test_y, return_counts = True))    # return_counts = 클래스별 몇 개 있는지
# 0 => 6000, 1=> 6000
# 0 => 티셔츠, 1 : 바지, 2: 스웨터, 3: 드레스, 4: 코트, 5: 샌달, 6: 셔츠

# import matplotlib.pyplot as plt

# print(train_x[0])
# print(train_x.shape)    # (60000, 28, 28)  => 한 이미지가 28*28이라는 뜻, 60000은 전체 이미지 개수
# # 수치가 0에 가까우면 검정색, 255에 가까우면 흰색

# plt.imshow(train_x[0], cmap='gray') # => 수치화 된 이미지를 보고 싶으면 imshow하면 됨! 
# plt.savefig('train_0.jpeg')

# 텐서플로우 (Batch, Height, Width, Channel) vs 파이토치 (Batch, Channel, Height, Width)
train_scaled = train_x.reshape(-1, 28, 28, 1)/255.0    #⭐ 이미지 데이터 정규화  # 여기서 -1은 이미지 개수(행)은 알아서 조정해달라는 이야기. 
print(train_scaled.shape)

# train / val dataset으로 분할하기 
from sklearn.model_selection import train_test_split
train_x, val_x, train_y, val_y = train_test_split(train_scaled, train_y, test_size = 0.2, random_state=42)

print(len(train_x)) # 48000개
print(len(val_x))   # 12000개
print(train_y.shape)

# ⭐ y를 category => One-Hot Encoding 해줘야 함 ⭐
from tensorflow.keras.utils import to_categorical   # 1 텐서플로우 케라스 도구함에서 원-핫 인코딩 변환기를 가져와라.
train_y = to_categorical(train_y, num_classes = 10)   # 2 기존의 정수형 train_y를 10개짜리 확률 배열 형태로 변환해서 다시 대입해라.
val_y = to_categorical(val_y, num_classes = 10)


# 모델 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten     # ⭐Dropout이랑 Flatten도
from tensorflow.keras.layers import Conv2D, MaxPooling2D

model = Sequential()
# conv2d ( filter 개수, 커널 사이즈, )
# 첫번째 : 필터 개수
# kernel_size ==> 3 (= 3 x 3)
# padding = 'same' ==> same padding=  zero padding
# input_shape = (28, 28, 1) 입력 이미지의 shape
# 첫번째 층은 항상 입력데이터를 생각해서 설계
# conv, layer 층 추가
model.add( Conv2D(filters=32, kernel_size=3, activation='relu', padding='same', input_shape = (28,28,1) ))    # 컨볼루션2d를 만들어서 추가

model.summary()

# Pooling Layer (풀링층) 추가
model.add( MaxPooling2D (2) )   # 2x2 필터가 2 스트라이드 이동하면서 최대값을 뽑는다는 뜻

# 다시 Conv Layer 층 추가
model.add ( Conv2D ( filters=64, kernel_size=(3, 3), activation='relu', padding='same'  ))

# Pooling Layer (풀링층) 추가
model.add( MaxPooling2D (2) )   # 2x2 필터가 2 스트라이드 이동하면서 최대값을 뽑는다는 뜻

# Flatten으로 평탄화 하기
model.add( Flatten() )

# FC layer 층 추가하기
model.add (Dense ( units = 100, activation='relu') )

# 과대적합 방지하기 위해 Dropout 추가
model.add( Dropout(0.4) ) # 학습된 가중치가 없음    #⭐여기서도 학습을 하는건가? 학습을 안하면 과대적합이 될 일이 없어서 dropout 안해도 될텐데 왜 dropout을 쓰는거지? 
model.add( Dense( 40, activation='relu'))

# 출력층 설계 => 분류하고자 하는 클래스의 수 만큼 뉴런 필요! 
# Fashion Mnist 데이터의 라벨(정답)이 => 10개 클래스로 분류
# 출력층의 활성화 함수는 다중 분류니깐 => softmax
model.add( Dense(10, activation='softmax' ))

model.summary()

# 모델 컴파일 (loss, optimizer, metrics)
model.compile( loss = 'categorical_crossentropy', optimizer='adam', metrics = ['accuracy'] )
              
# 콜백 기능 추가해서 best 모델 저장, 조기 종료 시키기
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping

modelpath = '/home/sophie/tf_env/fashioin_bestmodel.keras'
checkpointer_cb = ModelCheckpoint(filepath= modelpath, monitor='val_loss', save_best_only=True, verbose=1)
earlystop_cb = EarlyStopping(monitor = 'val_loss', patience=3, restore_best_weights=True)
 

# 모델 학습
ref = model.fit(train_x, train_y, batch_size = 64, epochs=100, verbose=1,   
        validation_data = (val_x, val_y), callbacks = (checkpointer_cb, earlystop_cb))

# ⭐ 이거 변수에 저장하는 건 나중에 시각화 할 때 써먹을라고 하는 거임


