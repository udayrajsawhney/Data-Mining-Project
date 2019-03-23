'''
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
# graph.render("iris", view=True)

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)
graph = graphviz.Source(dot_data) 
graph.format='' 
graph.render("iris",view=True)
'''
import pandas as pd
from sklearn import tree
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv('Iris.csv',sep= ',', header= None)

# print ("Dataset Lenght:: ", len(iris_data))
# print ("Dataset Shape:: ", iris_data.shape)
iris_feature_names = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
iris_target_names = ['Iris-setosa','Iris-versicolor','Iris-virginica']

X = iris_data.values[1:, 1:5]
Y = iris_data.values[1:,5]

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.1, random_state = 101)

# print(len(X_train))
# print(len(X_test))

clf_entropy = tree.DecisionTreeClassifier()
clf_entropy.fit(X_train, y_train)

dot_data = tree.export_graphviz(clf_entropy,out_file=None,
								feature_names=iris_feature_names,
								class_names=iris_target_names, 
								filled=True, 
								rounded=True,  
                         		special_characters=True)
graph = graphviz.Source(dot_data) 
graph.format='png' 
graph.render("iris",view=True)

y_pred_en = clf_entropy.predict(X_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)







