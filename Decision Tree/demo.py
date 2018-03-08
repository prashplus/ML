from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44],[177,90,43],[198,70,54],[182,79,43],[199,69,32],[175,75,43],[200,88,50],[188,52,10],[195,99,52],[185,59,32]]

Y = ['male','female','female','male','female','male','male','female','male','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction)