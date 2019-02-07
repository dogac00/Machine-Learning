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
        """
        finds the closest point
        in the training data
        to our specific row
        so that we find the nearest neighbor
        """
        
        best_dist = euc(self.X_train[0])  # initialize our distance to the very first data in our dataset
        best_index = 0                    # initialize our index to the very first index in our dataset
        
        for i in range(1, len(self.X_train)):  # iterate through the training data i.e. all the points on the plot
            dist = euc(row, self.X_train[i])   # find the euclidean distance between the specific row point and X_train[i]
            if dist < best_dist:
                best_dist = dist  # update the best distance
                best_index = i    # since we have found a closer one
                
        return self.y_train[best_index]
        
knn = KNN() # instantiate our classifier

# create random training samples

X_train = [[-10,-10],[-5,-5],[0,0],[5,5],[10,10]]
y_train = [0,0,0,1,1]

# fit our training data to our model

knn.fit(X_train, y_train)

knn.predict([[2,2],[7,7]]) # predict a sample

# this is an implementation of KNN where k = 1
# for k = 3 or k = 5 I think we have to use
# a couple of for loops and iterate through our training data
