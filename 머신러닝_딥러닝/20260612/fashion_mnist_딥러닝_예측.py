import numpy as np
from tensorflow.keras.datasets import fashion_mnist

# 데이터 준비하기
(train_x, train_y), (test_x, test_y) = fashion_mnist.load_data()
print(len(train_x), len(test_x))

# 시각화 해보기
# import matplotlib.pyplot as plt

# print(test_x[0])
# print(train_x.shape)    # (60000, 28, 28)  => 한 이미지가 28*28이라는 뜻, 60000은 전체 이미지 개수
# # 수치가 0에 가까우면 검정색, 255에 가까우면 흰색
# plt.imshow(train_x[0], cmap='gray') # => 수치화 된 이미지를 보고 싶으면 imshow하면 됨! 
# plt.savefig('test_0.jpeg')

# [퀘스트] test_0번껄로 이게 어떤 클래스인지 예측하기 => 클래스 이름이 직접 나와야함 ex) 구두, 가방 etc



# 소숫점 이하 3자리까지 출력
np.set_printoptions(precision=3, suppress=True)

# 1. 최고 성능 모델 불러오기
from tensorflow.keras.models import load_model
import joblib

best_model = load_model('/home/sophie/tf_env/fashioin_bestmodel.keras') 
best_model.summary()

# 2. test용 x 정규화 해주기
test_scaled = test_x.reshape(-1, 28, 28, 1) / 255.0    # 이미지는 255비트? 까지 있으니깐 연산할 때 쉽게 하기 위해서 255로 나눠줌. 
# ⭐ 왜 앞자리에 -1을 넣어주는 지 이해가 안감.

# 3. 0번째 이미지 한 장만 준비하기
target_image = test_scaled[0:1] 
# ⭐ 왜 [0] 이 아니고 [0:1] 로 가져와야하나? =>[0]을 쓰면 데이터가 3차원 덩어리가 되서 모델 에러남, 
# [0:1]이라고 적으면 모델이 원하는 4차원 박스 형태(배치 형태)를 그대로 유지할 수 있기 때문.

# 4. 예측 (Predict)
pred = best_model.predict(target_image)

# 5. 결과 확인하기

classes = ['티셔츠', '바지', '스웨터', '드레스', '코트', '샌달', '셔츠', '스니커즈', '가방', '앵클부츠']
classclf = np.array(classes)
print(classclf)

print("10개 클래스별 확률:", pred)
idx = np.argmax(pred, axis=1)

print("가장 확률이 높은 정답 번호:", np.argmax(pred))
print(classclf[np.argmax(pred, axis=1)])
print(classclf[idx])

