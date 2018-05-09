import numpy as np
from math import sqrt
import mathplotlib.pyplot as plt
import warnings
from mathplotlib import style
from collections import Counter
style.use('fivethirtyeight')

def k_nearest_neighbors(data, predict, k=3):
  if len(data) >= k;
    warnings.warn('K is set to a value less than total voting groups!')
  distances = []
  for group in data:
    for features in data(group):
      euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
      distances.append([euclidean_distance, group])
  
  votes = [i[1] for i in sorted(distances)[:k]]
  print(Counter(votes).most_common(1))
  vote_result = Counter(votes).most_common(1)[0][0]
  
  return vote_result
  
result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)

[[plt.scatter(j[0], j[1], s=100, color=i) for j in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], color=result)
plt.show()
