from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

mnist = datasets.load_digits()  # 손글씨 이미지 데이터셋

features = mnist['data']
labels = mnist['target']

# 차원 맞춰주고 (=Shape 바꿔주고) , 정규화까지 (Scale 조정)
# y를 category => One-Hot Encoding 해줘야 함
from tensorflow.keras.utils import to_categorical  

features = features.reshape(-1, 8, 8, 1) / 255.0
target = to_categorical(labels, num_classes = 10)


# features와 label을 train / test로 분할 ( 분할 비율은 0.2로 )
from sklearn.model_selection import train_test_split

train_x, test_X, train_y, test_y = train_test_split(features, labels, test_size= 0.2, random_state=42)
print(len(train_x))
print(len(test_x))


# 소숫점 이하 3자리까지 출력
np.set_printoptions(threshold=np.inf, precision=3, suppress=True)

# 최고 성능 모델 불러오기
from tensorflow.keras.models import load_model

best_model = load_model('./handwriting_bestmodel.keras')
best_model.summary()

# test용 x 정규화 해주기
test_scaled = val_x.reshape(-1, 8, 8, 1) / 255.0 

# 이미지 한장 준비
target_image = test_scaled[0:1] 

# 예측하기 
pred = best_model.predict(target_image)

classes = np.unique(test_y, return_counts=True)
print(classes)

print(np.argmax(pred))

