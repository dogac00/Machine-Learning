import sklearn import tree

# features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"][170, "bumpy"]]
# inputs to the classifier, but skicit-learn uses real-valued features

features = [[140, 1], [130, 1], [150, 0][170, 0]] # 0 for bumpy and 1 for smooth

# labels = ["apple", "apple", "orange", "orange"]
# output we want

labels = [0, 0, 1, 1] # 0 for apple and 1 for orange

# train classifier with a decision tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels) # find patterns in data

print(clf.predict([[150, 0]]))
