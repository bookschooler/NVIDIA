import numpy as np

# 데이터 준비 및 전처리
train_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260617/Covid19_CT_Image_dataset/train'
test_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260617/Covid19_CT_Image_dataset/test'

from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 4
img_size = 224

# train_이미지 증강 '틀' 생성
train_data_gen = ImageDataGenerator(
                    rescale = 1.0/255.,
                    rotation_range = 180,
                    width_shift_range = 0.2,
                    height_shift_range = 0.2,
                    horizontal_flip = True,
                    vertical_flip = True
)

# IMG 증강 데이터 불러와서 정말 증강 생성  (TEST 이미지)
train_img_gen = train_data_gen.flow_from_directory(
    train_dir, # 불러올 이미지 경로 
    batch_size=batch_size,
    shuffle=True,
    # 디렉토리 내부 이미지를 불러올 때 어떤 형식으로 라벨링해서 불러 올꺼냐 ~? 하는 것 
    class_mode = 'categorical',   # 이진 분류할 때 => 'binary' , if 다중분류면 => 'categorical'
    # save_to_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/cnn_cats_and_dogs_dataset/temp',
    # save_prefix = 'gen', # 증강이미지 파일명 앞에 'gen'을 붙여서 만들어라
    # save_format = 'jpg' , # 저장할 이미지 확장자 명시
    target_size = (img_size, img_size) #⭐ CNN 모델 입력 리사이즈 스펙
)                                 

# Test 이미지 생성틀 만들기
test_data_gen = ImageDataGenerator()

# Test 이미지 증강 생성 
test_img_gen = train_data_gen.flow_from_directory(
    train_dir, # 불러올 이미지 경로 
    batch_size = batch_size,
    shuffle = True,
    # 디렉토리 내부 이미지를 불러올 때 어떤 형식으로 라벨링해서 불러 올꺼냐 ~? 하는 것 
    class_mode = 'categorical',   # 이진 분류할 때 => 'binary' , if 다중분류면 => 'categorical'
    # save_to_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/cnn_cats_and_dogs_dataset/temp',
    # save_prefix = 'gen', # 증강이미지 파일명 앞에 'gen'을 붙여서 만들어라
    # save_format = 'jpg' , # 저장할 이미지 확장자 명시
    target_size = (img_size, img_size) #⭐ CNN 모델 입력 리사이즈 스펙
)

# 디렉토리 별 자동 레벨링 정보를 갖고 있음
print(train_img_gen.class_indices)

class_labels = list(train_img_gen.class_indices.keys())
print(class_labels[0], class_labels[1])

# VGG16 모델의 가중치를 가져와서 전이학습 하는 모델 설계

from tensorflow.keras.applications import vgg16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Flatten, Dense


# VGG16 모델의 Top층(FC를 의미)의 가중치는 가져오지마, 재설계 할꺼임
vgg16_cnn = vgg16.VGG16(weights = 'imagenet', include_top = False, input_shape = (img_size, img_size, 3))   # include_top 는 FC layer를 의미하는 거임
vgg16_cnn.summary()

# import os
# os.chdir('/home/sophie/tf_env/머신러닝_딥러닝/20260616/testimage_dataset')
# print(os.listdir())

# fileinfolist = []
# for file in os.listdir():
#     fileinfolist.append(img_dir + file)
# print(fileinfolist[0])

# CNN층에서 가져온 가중치 같은 건 학습 안되도록 Freeze시키기
for layer in vgg16_cnn.layers:
    layer.trainable = False     # ⭐vgg16 모델의 하단 cnn (특징추출하는 역할 레이어)는 학습안되게 설정

new_model = Sequential()
new_model.add (vgg16_cnn)
new_model.add (Flatten())
new_model.add (Dense (units = 1024, activation = 'leaky_relu'))
new_model.add (Dropout (0.3))
new_model.add (Dense(units=2, activation='softmax'))  # 위에 categorical로 읽어들여서 sigmoid말고 softmax로 해줘야함. 

new_model.summary()

# Compile 설정
import tensorflow as tf
optimizer = tf.keras.optimizers.Adam(learning_rate = 1e-6) # 0.0001
new_model.compile(loss = 'categorical_crossentropy', optimizer = optimizer, metrics = ['accuracy'])


import numpy as np
print(int(np.ceil(train_img_gen.samples / train_img_gen.batch_size)))
print( train_img_gen.samples )  # 총 데이터 수
print( train_img_gen.batch_size )   # 배치 사이즈

# 모델 조기종료 callback 준비
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint_cb = ModelCheckpoint('./ct_bestmodel.keras', save_best_only=True )
earlystop_cb = EarlyStopping(patience=3, restore_best_weights=True)

# 모델 학습시키기
record = new_model.fit(train_img_gen, 
            steps_per_epoch = int(np.ceil(train_img_gen.samples / train_img_gen.batch_size)),
            epochs = 30,
            validation_data= test_img_gen,
            validation_steps = int(np.ceil(test_img_gen.samples / test_img_gen.batch_size)),
            verbose = 1,
            callbacks = [checkpoint_cb, earlystop_cb]
            )

new_model.save('vgg16_newmodel.keras')

# 성능 시각화
import matplotlib.pyplot as plt

acc = record.history['accuracy']  # train 데이터의 정확도 
val_acc = record.history['val_accuracy'] # test 데이터의 정확도
loss = record.history['loss'] # test 데이터의 정확도
val_loss = record.history['val_loss'] # test 데이터의 정확도

# 새로운 이미지 예측 모델 만들기
from tensorflow.keras.preprocessing import image
import numpy as np

pred_list = [] 

def predict_vgg16_newmodel(new_model, filename): 
    img = image.load_img(filename, target_size=(224, 224)) 
    img_arr = image.img_to_array(img)  
    image_reshape = img_arr.reshape((1, 224, 224, 3))
    image_input = vgg16.preprocess_input(image_reshape) 

    # {'Covid': 0, 'Normal': 1}
    pred = new_model.predict(image_input, batch_size=1)  # 해당 이미지파일 예측
    print(pred)

    # 예측값이랑 클래스 이름 매칭시키기
    class_list = ['covid19', 'normal']
    print('pred result : ', class_list[np.argmax(pred)]) # 예측 최대 추정치 인덱스 추출
    pred_list.append( class_list[np.argmax(pred)] ) 


# 새 이미지 불러와서 예측 
import os
test_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260617/Covid19_CT_Image_dataset/test'
filenamelist = os.listdir(test_dir)  # 디렉토리 내부의 모든 파일 정보 리스트 반환
print(filenamelist)

file_totalinfo = []

for folder_name in filenamelist: 
    folder_path = os.path.join(test_dir, folder_name)    
    if os.path.isdir(folder_path):
        image_files = os.listdir(folder_path) 
        for file_name in image_files: 
            full_image_path = os.path.join(folder_path, file_name)             
            file_totalinfo.append(full_image_path) 
print(file_totalinfo) # 파일 경로 + 파일name 정보리스트 (이제 진짜 이미지 경로들이 출력됩니다)

for imagefile in file_totalinfo:
    predict_vgg16_newmodel(new_model, imagefile) 