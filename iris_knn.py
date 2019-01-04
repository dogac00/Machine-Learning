from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()

X_train = iris.data
y_train = iris.target

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

y_test = knn.predict(X_test)

# for explanations look at the iris_logistic_regression.py file.
