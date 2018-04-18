import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

X=np.array([-80.7,-75.4,-80.2,-77.5,-84.1,-85.6,-83.3,-82.8,-89.5,-80.8,-86.2,-88.4,-82.8,-86.3,-85.6,-86.1,-93.2,-81.9,-85.2,-90.2,-93.3,-92.2,-92.8]) # average rssi values for a specific distance
Y=np.array([214,310,330,365,405,430,465,495,545,585,610,670,720,785,835,910,990,1050,1120,1212,1305,1450,1600]) # distance values

# fit into polynom
polinom_coefficient = np.polyfit(X, Y, 2)

a=polinom_coefficient[0]
b=polinom_coefficient[1]
c=polinom_coefficient[2]

# evenly spaced numbers over the interval
xval = np.linspace(np.min(X), np.max(X))   

# calculate polynomial regression
regression = a * xval**2 + b*xval + c 

# get the number and calculate the polynomial prediction
predX = float(input("Enter RSSI: "))      
predY = a * predX**2 + b*predX + c   

plt.scatter(X,Y, s=20, color="blue" )      
plt.scatter(predX, predY, color="red")    
plt.plot(xval, regression, color="black", linewidth=1)      

print("Estimated Distance: ", predY)
