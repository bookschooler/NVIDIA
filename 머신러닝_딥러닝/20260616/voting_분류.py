from sklearn import datasets
from sklearn import tree # 의사 결정 트리 모델  => 불순도가 낮아지는 방향으로 트리를 성장시켜서 분류
from sklearn.neighbors import KNeighborsClassifier  # KNN 분류 모델 
# KNN 분류 모델 => K 개의 최근접 이웃이 뭐니? 
# SVM => 결정경계를 활용한 분류 모델
from sklearn.svm import SVC     # SVM 모델 
# 나이브 베이즈 => 조건부 확률로 분류

from sklearn.ensemble import VotingClassifier # 보팅분류
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mnist = datasets.load_digits()   # 손글씨 데이터 ( 0-9로 이루어진 손글씨 이미지 데이터 )
print(mnist)


features = mnist['data']
labels = mnist['target']
print(len(features)) # 1797
print(len(labels)) # 1797

train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size=0.2)

# Tree 모델 
tree_model = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=8,
                                         max_features=32, random_state=42)
tree_model.fit(train_x, train_y)
print('tree acc: ', tree_model.score(test_x, test_y))    # acc: 0.85

# KNN 모델
knn_model = KNeighborsClassifier( n_neighbors=299)
knn_model.fit(train_x, train_y)
print('knn acc: ', knn_model.score(test_x, test_y))    # acc: 0.85

# SVM 모델
svm_model = SVC(C=0.1, gamma=0.003, probability=True, random_state=42)
svm_model.fit(train_x, train_y)
print('svc acc: ', svm_model.score(test_x, test_y))    # acc: 0.925

# Hard Voting 정확도
hardvoting_model = VotingClassifier(estimators=[
    ('decision_tree', tree_model),
    ('knn', knn_model),
    ('svm', svm_model)], weights = [1, 1, 1], voting='hard'
    )

hardvoting_model.fit(train_x,train_y)
print('hardvoting acc: ', hardvoting_model.score(test_x, test_y))    # 0.94

# Soft Voting 정확도
softvoting_model = VotingClassifier(estimators=[
    ('decision_tree', tree_model),
    ('knn', knn_model),
    ('svm', svm_model)], weights = [1, 1, 1], voting='soft'
    )

softvoting_model.fit(train_x,train_y)
print('softvoting acc: ', softvoting_model.score(test_x, test_y))    # 0.91
