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

print(features.shape)   # (1797, 8, 8, 1) => (batch_size, h_img, v_img, channel)

# 차원 맞춰주고 (=Shape 바꿔주고) , 정규화까지 (Scale 조정)
features = features.reshape(-1, 8, 8, 1) / 255.0
print(features[0])

# features와 label을 train / test로 분할 ( 분할 비율은 0.2로 )
from sklearn.model_selection import train_test_split
train_x, val_x, train_y, val_y = train_test_split(features, labels, test_size= 0.2, random_state=42)
print(len(train_x))
print(len(val_x))

print(val_x[0])
print(val_y[0]) 

# y를 category => One-Hot Encoding 해줘야 함
from tensorflow.keras.utils import to_categorical  
train_y = to_categorical(train_y, num_classes = 10)  
val_y = to_categorical(val_y, num_classes = 10)
print(val_y.shape)
# 데이터 전처리 및 데이터 준비 완료

# 새로운 데이터 생성
new_data = np.array([
    [0., 0., 5., 13., 9., 1., 0., 0.],
    [0., 0., 13., 15., 10., 15., 5., 0.],
    [0., 3., 15., 2., 0., 11., 8., 0.],
    [0., 4., 12., 0., 0., 8., 8., 0.],
    [0., 5., 8., 0., 0., 9., 8., 0.],
    [0., 4., 11., 0., 1., 12., 7., 0.],
    [0., 2., 14., 5., 10., 12., 0., 0.],
    [0., 0., 6., 13., 10., 0., 0., 0.]
])
new_data1 = features[0:5]

new_data = np.array(new_data).reshape(-1, 8, 8, 1)/255.0


# best 모델 불러오기 
from tensorflow.keras.models import load_model
best_model = load_model('./handwriting_bestmodel.keras')

# 소숫점 이하 3자리까지 출력
np.set_printoptions(threshold=np.inf, precision=3, suppress=True)

# 예측 (Predict)
pred = best_model.predict(new_data)
pred = best_model.predict(val_x[0:5])

# y 클래스 매칭해주기 
classes = np.unique(val_y)
print(classes)
print(np.argmax(pred, axis=1))




