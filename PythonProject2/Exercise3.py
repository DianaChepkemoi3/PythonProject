import sys
import numpy as np

def main():
    a = np.array([[5,9],
                  [7,2]])

    b = np.array([[3,8],
                  [4,6]])

    print("Matrix a: ", a)
    print("Matrix b: ", b)

    addition_result = a + b
    print("Elementwise addition: ", addition_result)

    multiplication_result = a * b
    print("Elementwise multiplication: ", multiplication_result)

    matmul_result = a@b
    print("Matrix product (a @ b): ", matmul_result)

    return 0

if __name__ == "__main__":
    sys.exit(main())