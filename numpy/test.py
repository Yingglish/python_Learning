import numpy as np


x0 = np.arange(-2, 2.5, 0.25)
x1 = np.arange(-2, 2.5, 0.25)
X, Y = np.meshgrid(x0, x1)

# print(np.meshgrid(x0, x1))

X = X.flatten() #
Y = Y.flatten()
# print(X)
# print("\n")
# print(Y)
Z  = np.array([X, Y])
print(Z.ndim) # 
