
from multiprocessing import Pool, cpu_count
import time

def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            print(n, i)
            factors.append(i)
    return factors

def factorize(*number):    
    result = []
    for num in number:
        result.append(factorize_number(num))
    return result 
    
start_time = time.time()
a, b, c, d = factorize(12823, 23255, 99999, 10651060)
end_time = time.time()

print("Parallel version time:", end_time - start_time, "seconds")
