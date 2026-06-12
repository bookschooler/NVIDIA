import pickle
import joblib
import numpy as np
import pandas as pd  
from tensorflow.keras.models import load_model  

# 소수점 3자리까지 출력해라
np.set_printoptions(precision=3,suppress=True)

#  저장된 딥러닝 모델과 피클 스케일러 불러오기
fish_bestmodel = load_model('/home/sophie/tf_env/fish_multi_classify.keras')  # 4  # 딥러닝 모델을 로드합니다.

#  "titanic_Scaler.pkl" 파일을 바이너리 읽기(rb) 모드로 열어서 스케일러 복원하기
load_scaler = joblib.load(
    "fish_scaler.pkl")

# 2. 예측할 새로운 데이터 준비 
new_data = { 
    'Weight': [340, 9.8, 200, 150, 110],  
    'Length': [26.5, 11.4, 32.0, 22.0, 21.0],  
    'Diagonal': [31.1, 12.0, 35.5, 24.5, 22.5],  
    'Height': [12.38, 2.08, 5.08, 6.44, 5.69],   
    'Width': [4.67, 1.27, 2.77, 3.80, 3.56]   
}

 # 12  # 딕셔너리 정의를 마칩니다.
my_df = pd.DataFrame(new_data, index=['A', 'B', 'C', 'D', 'E'])  # 13  # 데이터프레임으로 변환합니다.

# 3. 불러온 스케일러로 데이터 변환 진행 (이미 fit이 완료된 상태이므로 transform만 수행!)
my_scaled = load_scaler.transform(my_df.to_numpy())  # 14  # 데이터프레임을 넘파이 배열로 바꿔 해동된 스케일러로 변환합니다.

# 4. 최종 예측
my_predict = fish_bestmodel.predict(my_scaled)  # 15  # 변환된 데이터를

print(my_predict)

fishclass = ['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish']
np.array(['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish'])

# print(np.argmax(my_predict))
best_indices  = np.argmax(my_predict, axis = 1) # 최대값의 인덱스로 이루어진 넘파이 배열(list)이 만들어짐

print( )

for idx, fish_idx in enumerate(best_indices):
    print(f"물고기 {my_df.index[idx]}: {fishclass[fish_idx]}")