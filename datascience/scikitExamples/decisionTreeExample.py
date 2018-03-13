from sklearn import tree
'''
feature     label
140,1,      1
130,1,      1
150,0,      0
170,0,      0
145,1       1
'''

features= [[140,1],[130,1],[150,0],[170,0]]   #0 bumpy, 1 smooth

labels= [0,0,1,1]       #0 orange, 1 apple


clf= tree.DecisionTreeClassifier()
clf= clf.fit(features,labels)


print ( clf.predict([[145,1]]) )