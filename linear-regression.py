from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

x = np.array([112, 245, 198, 305, 372, 550, 302, 420, 578])
y = np.array([1120, 1553, 2102, 2230, 2600, 3200, 3409, 3629, 4460])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x,y,'ro',color='black')
plt.ylabel('Price')
plt.xlabel('Size of house')

plt.axis([0,600,0,5000])

plt.plot(x, x*slope*intercept, 'b')

// PREDICTION
newX = 150
newY = newX*slope*intercept

print(newY)

plt.plot()
plt.show()

/* The program will show the prediction value for our newX value and the program will show the
linear regression line in blue color in our graph and also intercepts are shown with black. */

