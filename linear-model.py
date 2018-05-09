import numpy as np
import mathplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0 # a random guess: random value, 1.0

# our model for the forward pass
def forward(x):
  return x*w
  
# loss function
def loss(x, y):
  y_pred = forward(x)
  return (y_pred - y) * (y_pred - y)
  
w_list = []
mse_list = []

for w in np.arrange(0.0, 4.1, 0.1):
  print("w = ", w)
  l_sum = 0
  for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    l = loss(x_val, y_val)
    l_sum += l
    print("\t", x_val, y_val, y_pred_val, 1)
  print("MSE = ", l_sum / 3)
  w_list.append(w)
  mae_list.append(l_sum / 3)
  
plt.plot(w_list, mae_list)
plt.ylabel("Loss")
plt.xlabel("w")
plt.show()
