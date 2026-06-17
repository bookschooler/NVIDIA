train_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/cnn_cats_and_dogs_dataset/train'

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 이미지 증강 유형 생성
train_img_gen = ImageDataGenerator(
                    rescale = 1.0/255.,
                    rotation_range = 20,
                    height_shift_range = 0.2,
                    horizontal_flip = True,
                    shear_range = 0.3)

# image 읽어 들이면서 img 증강시켜주는 제너레이터 생성
train_data_gen = train_img_gen.flow_from_directory(
    train_dir, # 불러올 이미지 경로 
    batch_size=2,
    shuffle=False,
    save_to_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260615/cnn_cats_and_dogs_dataset/temp',
    save_prefix = 'gen', # 증강이미지 파일명 앞에 'gen'을 붙여서 만들어라
    save_format = 'jpg' , # 저장할 이미지 확장자 명시
    target_size = (150, 150) #⭐ CNN 모델 입력 리사이즈 스펙
)

i=0
for b in train_data_gen:
    i += 1
    if i > 2 :
        break

