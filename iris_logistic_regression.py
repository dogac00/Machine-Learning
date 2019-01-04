from sklearn.datasets import load_iris # we import the load_iris method

iris = load_iris() # we instantiate the method

X_train = iris.data # we create a X_train matrix variable for the attribute data
y_train = iris.target # we create a y_train vector variable for the attribute target

print(X_train.shape)
print(Y_train.shape)

# you can see shapes of X_train and y_train by printing them

# we can use logistic regression model to fit and predict

logreg = LogisticRegression() # create an instance of the classifier

logreg.fit(X_train, y_train) # we fit the X_train and y_train to the model

y_test = logreg.predict(X_test) # and lastly, we predict the y_test variable
