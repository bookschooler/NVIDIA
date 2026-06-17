# 랜덤 포레스트_의사결정트리 정확도 성능 비교
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

mnist = load_digits()

print(mnist['data'][:3])
print(len(mnist['data']))
print(mnist['target'])
print(len(mnist['target']))

# X, Y 할당
features = mnist['data']
labels = mnist['target']

from sklearn.model_selection import cross_validate
rf_model = RandomForestClassifier()
rf_scores = cross_validate(rf_model, features, labels, cv=10)
print(rf_scores['test_score'])

dt_scores = cross_validate(tree.DecisionTreeClassifier(), features, labels, cv=10)
print(dt_scores)

import numpy as np
print('random_forest accuracy: ', np.mean(rf_scores['test_score']))
print('decision_tree accuracy: ', np.mean(dt_scores['test_score']))

import pandas as pd
df = pd.DataFrame( {'random_forest':rf_scores['test_score'], 
                   'decision_tree':dt_scores['test_score'] })

print(df)
df.plot()
plt.show()

