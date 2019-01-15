from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class KNN():
    def fit(self, X_train, y_train):
        """
        fits or trains our training data
        """
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_test):
        """
        predicts values for test values
        and put them into an array
        and return it
        """
        predictions = []
        
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        
        return predictions
    
    def closest(self, row):
        best_dist = euc(self.X_train[0])
        best_index = 0
        
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
                
        return self.y_train[best_index]
        
knn = KNN() # instantiate our classifier

# create random training samples

X_train = [[-10,-10],[-5,-5],[0,0],[5,5],[10,10]]
y_train = [0,0,0,1,1]

# fit our training data to our model

knn.fit(X_train, y_train)

knn.predict([[2,2],[7,7]]) # predict a sample

# this is an implementation of KNN where k = 1
# for k = 3 or k = 5 I think we have to
# use a couple of for loops and iterate our training data
