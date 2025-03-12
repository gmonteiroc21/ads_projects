import time

def calc_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1)**i) / (2*i + 1)
    return pi * 4

def test_float_operations(limit):
    start_time = time.time()
    calc_pi(limit)
    end_time = time.time()
    print(f"Tempo de execução para calcular pi com {limit} iterações: {end_time - start_time} segundos.")
    
test_float_operations(100000)
