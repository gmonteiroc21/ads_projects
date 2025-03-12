import time
import numpy as np

def matrix_multiplication(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    start_time = time.time()
    np.dot(A, B)
    end_time = time.time()
    print(f"Tempo de execução para multiplicação de matrizes {size}x{size}: {end_time - start_time} segundos.")
    
matrix_multiplication(500)
