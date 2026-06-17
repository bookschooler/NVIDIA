from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
mnist = load_digits()
print(mnist['data'][-3:])
print(mnist['target'][-3:])

features = mnist['data']    # 1797개의 8*8 이미지 데이터셋
labels = mnist['target']

rf_model = RandomForestClassifier()
rf_model.fit(features, labels)

print('score:', rf_model.score(features, labels))

pred = rf_model.predict(features[-5:])
print('labels: ', labels[-5:])
print('pred: ', pred)

tempdata = [0., 0., 10., 14., 8., 1., 0., 0., 0., 2., 16., 14., 6., 15., 6., 0., 0., 0.,
            12., 15., 8., 15., 0., 0., 0., 15., 5., 16., 16., 10., 0., 0., 0., 0., 12., 15.,
            13., 12., 0., 0., 0., 4., 16., 5., 4., 16., 6., 0., 0., 8., 16., 10., 8., 16.,
            8., 1., 0., 11., 7., 12., 14., 12., 1., 0.]

import numpy as np
import matplotlib.pyplot as plt
temparr = np.array(tempdata) # reshape해야되서 일단 array로 변환
print(temparr)
print(temparr.shape)
temp_pred = rf_model.predict([temparr])

print('temp_pred : ', temp_pred)

plt.imshow(temparr.reshape(8,8))
plt.show()
