from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )

print(euclidean_distance)

# this will only calculate nearest neighbors on two feature dimensions
# for more, you can look at my k-nearest-neighbors algorithm
