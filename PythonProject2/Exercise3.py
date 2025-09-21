import numpy as np

A = np.array([[5,9],
              [7,2]])

B = np.array([[3,8],
              [4,6]])

print("Matrix A: ", A)
print("Matrix B: ", B)

addition_result = A + B
print("Elementwise addition: ", addition_result)

multiplication_result = A * B
print("Elementwise multiplication: ", multiplication_result)

matmul_result = A@B
print("Matrix product (A @ B): ", matmul_result)
