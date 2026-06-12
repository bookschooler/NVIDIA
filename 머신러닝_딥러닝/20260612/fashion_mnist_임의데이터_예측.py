import cv2       # opencv-python
import numpy as np

img = cv2.imread('/home/sophie/tf_env/머신러닝_딥러닝/20260612/sandal_1.jpg', cv2.IMREAD_GRAYSCALE)
print(img)

# numpy 찾아서 ... 안보이게 풀 출력하기
np.set_printoptions(precision=8, suppress=True)
np.set_printoptions(threshold=np.inf)   # 데이터 많을 때 중간에 줄임표 ...  안쓰고 다 출력해랏! 
print(img)
print(img.shape)    # 이미지 사이즈 330x330  => 얘를 28x28 사이즈로 맞춰줘야함.(학습한 모델은 28x28 이므로)

# 이미지를 그냥 축소할 순 없으니깐 보간(보합)? 법을 써줘서 축소해야함. => 이미지 리사이징
img_resize = cv2.resize(img, dsize = (28, 28), interpolation=cv2.INTER_AREA )  
print(img_resize.shape)

# 이미지 출력해서 확인해보기
# import matplotlib.pyplot as plt
# plt.imshow(img_resize, cmap='gray')
# plt.savefig('sandal_resize.jpeg')

# 이미지 색상 반전
img_reverted = cv2.bitwise_not(img_resize)

# 이미지 출력해서 확인해보기
# import matplotlib.pyplot as plt
# plt.imshow(img_resize, cmap='gray')
# plt.savefig('sandal_reverted.jpeg')

img_reverted = img_reverted/255.0   # 스케일 변환
print(img_resize.shape) # => (28, 28)로 나오는데 (28, 28, 1)로 변환해줘야함.quit
img_reverted = img_reverted.reshape(1, 28, 28, 1) # ⭐ 여기 왜 이렇게 바꾸는 지 확인

# 소숫점 이하 3자리까지 출력
np.set_printoptions(precision=8, suppress=True)

# 만들어 놓은 모델 가져오기
from tensorflow.keras.models import load_model

best_model = load_model('/home/sophie/tf_env/fashioin_bestmodel.keras') 
best_model.summary()

# 위에서 생성한 임의의 데이터 예측
pred = best_model.predict(img_reverted)
print(pred)

# 예측 결과 클래스 이름으로 나타내기

classes = ['티셔츠', '바지', '스웨터', '드레스', '코트', '샌달', '셔츠', '스니커즈', '가방', '앵클부츠']
classclf = np.array(classes)    
idx = np.argmax(pred, axis=1)
print("가장 확률이 높은 정답 번호:", np.argmax(pred))
print(classclf[np.argmax(pred, axis=1)])
print(classclf[idx])




