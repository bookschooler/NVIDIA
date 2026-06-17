## 예측 시켜볼 데이터 불러오고 전처리 ##
import cv2       # opencv-python
import numpy as np

img = cv2.imread('/home/sophie/tf_env/머신러닝_딥러닝/20260615/baekgu.jpg', cv2.IMREAD_COLOR_RGB)
print(img)

# numpy 찾아서 ... 안보이게 풀 출력하기
np.set_printoptions(precision=8, suppress=True, threshold=np.inf)   # 데이터 많을 때 중간에 줄임표 ...  안쓰고 다 출력해랏! 
print(img)
print(img.shape)    # 이미지 사이즈 467x566  => 얘를 150x150 사이즈로 맞춰줘야함.

# 이미지를 보간(보합)? 법을 써줘서 축소해야함 => 이미지 리사이징
img_resize = cv2.resize(img, dsize = (150, 150), interpolation=cv2.INTER_AREA )  
print(img_resize.shape)

#  이미지 출력해서 확인해보기
import matplotlib.pyplot as plt
plt.imshow(img_resize)
plt.savefig('baekgu_resize.jpeg')

# 스케일 변환
img_scaled = img_resize/255.0
print(img_scaled.shape) 
img_scaled = img_scaled.reshape(-1, 150, 150, 3) # ⭐ 여기 왜 이렇게 바꾸는 지 확인


# 만들어 놓은 모델 가져오기
from tensorflow.keras.models import load_model

best_model = load_model('./catdog_bestmodel.keras') 
best_model.summary()

# 백구 사진 예측
pred = best_model.predict(img_scaled)
print(pred)
print(pred.shape)
print(pred[0])
print(pred[0][0])
# y 클래스 매칭해주기 

if pred[0][0] > 0.5:
    print("dogs")
else:
    print("cats")


# classes_info = {'cats': 0, 'dogs': 1}
# labels_list = list(classes_info.keys()) # => [cats, dogs]

# pred_idx = np.argmax(pred, axis=1)[0]
# # pred_label = labels_list[pred_idx]
# print(pred_idx)

# # if pred_idx[0][0] > 0.5:
# #     print("dogs")
# # else:
# #     print("cats")


