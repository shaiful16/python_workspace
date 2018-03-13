from builtins import print

import graphviz
from sklearn.datasets import load_iris
import numpy as np
from sklearn import datasets,tree

iris = datasets.load_iris()
# setosa, versicolor, virginica
#print(iris.data)
#print(iris.target)
#print(iris.data[0])
#print(iris.target[0])

test_index=[0,50,100]

#training
train_data=np.delete(iris.data,test_index,axis=0)
train_target=np.delete(iris.target,test_index)

#testing
test_data=iris.data[test_index]
test_target=iris.target[test_index]


clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

#print(test_data)
print(test_target)
print(clf.predict(test_data))


import graphviz
dot_data = tree.export_graphviz(clf, out_file=None,  feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
