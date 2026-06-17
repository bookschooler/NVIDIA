import pandas as pd
from sklearn.datasets import load_iris  #붓꽃 데이터셋 <= 가우시안 써볼라고 사용 
from sklearn.model_selection import train_test_split # train/test 분리할 때 사용


from sklearn.naive_bayes import GaussianNB  # 데이터 특징이 정규분포일 때 분류 모델로 사용! 
# 분류 모델 => GaussianNB
from sklearn import metrics # 혼동행렬 
from sklearn.metrics import accuracy_score # 정확도
# score 메소드가 다 해주긴 하지만 그래도 직접적으로 보려면 import하는 게 ... 

dataset = load_iris()
print(dataset)


# 모델에 학습 시킬 준비 데이터셋 준비
# train/ test 셋 분리
train_x, test_x, train_y, test_y = \
    train_test_split(dataset['data'], dataset['target'], test_size = 0.2, random_state=42)

print(train_x[:5])
print(test_x[:5])

# 가우시안 나이브베이즈 모델 준비
gnb_model = GaussianNB()

# 모델 학습
gnb_model.fit(train_x, train_y)

# 예측 
pred = gnb_model.predict(test_x[:3])
print('예측값: ', pred)
print('실제 정답: ', test_y[:3])

# 성능 평가
print('test acc:', gnb_model.score(test_x, test_y))    # 모델 성능 평가 

# 새로운 데이터 3개 추가해서 예측




