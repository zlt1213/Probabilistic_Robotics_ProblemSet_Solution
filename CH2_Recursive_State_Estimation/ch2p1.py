import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# define the matrix
A = np.array([[1.0,1.0], [0.0, 1.0]])
R = np.array([[0.25,0.5], [0.5, 1]])
print("Matrix A:")
print(A)
print("\nMatrix R:")
print(R)

sigma_bar = np.zeros([2,2,6])

for i in range(5):
    if i == 0:
        1;
    else:
        sigma_bar[:,:,i] = np.dot( np.dot(A, sigma_bar[:,:,i-1]), A.transpose()) + R
    print("\nsigma_bar: " + str(i))
    print(sigma_bar[:,:,i])






















 ##
