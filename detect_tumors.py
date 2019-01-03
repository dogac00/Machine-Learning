import numpy as np
import random
from sklearn.linear_model import LogisticRegression

patients = np.zeros((15,2)) # generate a numpy array with zeros with specified dimensions

for patient in patients:
    patient[0] = random.choice((0,1))
    patient[1] = random.randint(18,80)
    
# give random choices of male or female choices to first column
# and give random integers btw 18 to 80 to second column

results = np.random.randint(0,2,(15,))
# generate random results

logreg = LogisticRegression()
# instantiate a logreg instance

logreg.fit(patients, results)
# fit patients and results to the instance

print(logreg.predict([[1,74],[0,23],[0,15],[0,34],[1,233],[0,55]]))
# print my testing data, this could be a data from a hospital
