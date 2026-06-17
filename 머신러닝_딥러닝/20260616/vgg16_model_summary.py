from tensorflow.keras.applications import vgg16

vgg16_model = vgg16.VGG16()
vgg16_model.summary()

img_dir = '/home/sophie/tf_env/머신러닝_딥러닝/20260616/testimage_dataset/'

import os
os.chdir('/home/sophie/tf_env/머신러닝_딥러닝/20260616/testimage_dataset')
print(os.listdir())

fileinfolist = []
for file in os.listdir():
    fileinfolist.append(img_dir + file)
print(fileinfolist[0])

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

img = load_img(fileinfolist[0], target_size = (224, 224))
img = img_to_array(img) # 이미지 객체를 넘파이 배열로 변경
print(img.shape)

img = img.reshape(-1, 224, 224, 3)
print(img.shape)

img = vgg16.preprocess_input(img)   # 알아서 정규화도 해주고, rgb 색상도 맞춰줌
print(img)

pred = vgg16_model.predict(img)
print(pred)
print(len(pred[0]))

labels = vgg16.decode_predictions(pred)
print(labels)
