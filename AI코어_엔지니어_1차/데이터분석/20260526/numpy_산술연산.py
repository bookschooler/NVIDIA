import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array( [ [5,6],[3,7] ])
print(arr1)
arr2 = np.array( [ [3,4],[2,5] ])
print(arr2)
print( arr1 + arr2 )

arr3 = np.array([3,4,5])
print(arr3 + 3)

arr4 = np.linspace(1,10, 5)
# 메모리에 차트를 랜더링
arr5 = np.array([1,3,6,10,15])
plt.plot(arr5)
plt.show() # 메모리에 랜더링된 차트를 화면에 출력해줘