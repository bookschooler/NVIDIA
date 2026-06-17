from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비 및 전처리
train_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/intel_dataset/seg_train/seg_train'
test_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/intel_dataset/seg_test/seg_test'

from tensorflow.keras.preprocessing.image import ImageDataGenerator


# train_이미지 증강 '틀' 생성
train_img_gen = ImageDataGenerator(
                    rescale = 1.0/255.,
                    rotation_range = 50,
                    height_shift_range = 0.3,
                    horizontal_flip = True,
                    shear_range = 0.3)

test_img_gen = ImageDataGenerator(rescale = 1.0/255.)

# IMG 증강 데이터 불러와서 정말 증강 생성  (TEST 이미지)
train_data_gen = train_img_gen.flow_from_directory(
    train_dir, # 불러올 이미지 경로 
    batch_size= 100,
    shuffle=True,
    # 디렉토리 내부 이미지를 불러올 때 어떤 형식으로 라벨링해서 불러 올꺼냐 ~? 하는 것 
    class_mode = 'categorical',   # 이진 분류할 때 => 'binary' , if 다중분류면 => 'categorical'
    # save_to_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/intel_dataset/temp',
    # save_prefix = 'gen', # 증강이미지 파일명 앞에 'gen'을 붙여서 만들어라
    # save_format = 'jpg' , # 저장할 이미지 확장자 명시
    target_size = (150, 150) #⭐ CNN 모델 입력 리사이즈 스펙
)

# IMG 증강 데이터 불러와서 정말 증강 생성  (TEST 이미지)
test_data_gen = test_img_gen.flow_from_directory(
    test_dir, # 불러올 이미지 경로 
    batch_size=100,
    shuffle=True,
    # 디렉토리 내부 이미지를 불러올 때 어떤 형식으로 라벨링해서 불러 올꺼냐 ~? 하는 것 
    class_mode = 'categorical',   # 이진 분류할 때 => 'binary' , if 다중분류면 => 'categorical'
    # save_to_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/intel_dataset/temp',
    # save_prefix = 'gen', # 증강이미지 파일명 앞에 'gen'을 붙여서 만들어라
    # save_format = 'jpg' , # 저장할 이미지 확장자 명시
    target_size = (150, 150) #⭐ CNN 모델 입력 리사이즈 스펙
)

# Y 어떻게 분류했나 알아보기
print(test_data_gen.class_indices)
# print(test_data_gen.shape)
print(train_data_gen.samples)   # => 14034 
print(test_data_gen.samples)    # => 3000


# 모델 준비 및 설계
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling2D

model = Sequential()
model.add( Conv2D( filters=32, kernel_size=(3,3), activation='leaky_relu', padding = 'valid', input_shape = (150, 150, 3)))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Conv2D( filters = 64, kernel_size=(3,3), activation='leaky_relu'))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Conv2D( filters = 128, kernel_size=(3,3), activation='leaky_relu'))
model.add ( MaxPooling2D(pool_size = (2,2)))
model.add( Flatten())
model.add( Dense( units = 512, activation='relu'))
model.add( Dropout(0.3))
model.add( Dense( units = 6, activation='softmax'))
model.summary()

# 모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# 모델 조기종료 callback 준비
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint_cb = ModelCheckpoint('./intel_bestmodel.keras', save_best_only=True )
earlystop_cb = EarlyStopping(patience=3, restore_best_weights=True)

# 모델 학습( Generator를 활용)
# steps_per_epoch = 200 => 총 train 데이터 4000개 나누기 batch_size 20 => 200
record = model.fit(train_data_gen, validation_data = test_data_gen, 
                    steps_per_epoch = 1400, validation_steps = 300,
                    verbose=1, epochs = 50,
                    callbacks = [checkpoint_cb, earlystop_cb])

# 성능 시각화
import matplotlib.pyplot as plt

acc = record.history['accuracy']  # train 데이터의 정확도 
val_acc = record.history['val_accuracy'] # test 데이터의 정확도
loss = record.history['loss'] # test 데이터의 정확도
val_loss = record.history['val_loss'] # test 데이터의 정확도

epochs = np.arange(len(acc))
plt.figure()
plt.plot(epochs, loss, 'b', label = 'Train loss')
plt.plot(epochs, val_loss, 'g', label = 'Val_loss' )
plt.legend()
plt.savefig('catdog_model.jpeg')
657