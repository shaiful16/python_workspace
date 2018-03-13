
from numpy import genfromtxt
from sklearn import tree


features= genfromtxt('E:/WorkSpace/python_workspace/datascience/pandasExamples/laptop.csv', delimiter=',')
labels= [10,20,30,40]

clf= tree.DecisionTreeClassifier()
clf= clf.fit(features,labels)
print ( clf.predict([[13,0,4]]) )
print ( clf.predict([[15,1,5]]) )
print ( clf.predict([[14,1,4]]) )