import numpy as np


fruit = ['사과', '바나나', '포도', '딸기']

# print(fruit[0:1]) 
# print(fruit[[0,2]]) # 에러 남 => 리스트의 [  ]  <= 여기 안에는 정수 아니면 1:3 이런 형태만 올 수 있음. 

# # 리스트에서 fruit[1] => 원소 알맹이 하나만 나옴.  ex) 사과
# # 리스트에서 fruit[0:1] => 리스트까지 살아서 나옴.  ex) ['사과']

fruit_num = np.array(['사과', '바나나', '포도', '딸기'])
print(fruit_num.shape)  # shape이 (4, )

# print(fruit_num[0])     # 원소 하나만 나옴          ex) 사과
# print(fruit_num[0:1])   # 리스트까지 살아서 나옴     ex) ['사과']
print(fruit_num[ [0,2] ]) 