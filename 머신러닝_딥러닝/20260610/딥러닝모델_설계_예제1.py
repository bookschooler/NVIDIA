
import tensorflow as tf
from tensorflow.keras.layers import Dense # 새로운 층 만들 때 사용
from tensorflow.keras.models import Sequential

model = Sequential()    # 딥러닝 층을 추가할 수 있는 전체 틀 생성
# Dense()의 첫 파라미터는 해당 층의 뉴런의 개수를 지정
model.add(Dense(30, input_dim=4, activation='sigmoid')) # 뉴런 30개, 입력값 4개, 활성화함수는 시그모이드 
model.add(Dense(1, activation='sigmoid'))   
#⭐여기에 input_dim이 없는 이유는 이미 그 전 층에 뉴런 수가 30개인 걸 알고 있기 때문

# 모델이 잘 설계 됐는지 체크
model.summary()

# 모델의 효과적 학습을 위한 환경설정. 손실함수, 활성화함수 등의 매트릭스 정의
model.compile(optimizer='adam', loss='mse', metrics='accuracy')






