import numpy as np

mylist = [-6.5, 1.03, 5.16, 3.34, 0.33, -0.63]
arr = np.array(mylist)

exp_a = np.exp(arr)
sum_exp_a = np.sum(exp_a)

y = exp_a / sum_exp_a
print(np.round(y, decimals=3))
print(y)


# 확률이 가장 큰 index를 출력
max_index = np.argmax(y) 
print(f'최고 확률 index: {max_index}')
print(f'최고 확률 값: {y[max_index]:.4f}')  #⭐기억하기!!!
