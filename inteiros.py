import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_prime_operations(limit):
    start_time = time.time()
    primes = [n for n in range(limit) if is_prime(n)]
    end_time = time.time()
    print(f"Tempo de execução para encontrar números primos até {limit}: {end_time - start_time} segundos.")
    
test_prime_operations(10000)
