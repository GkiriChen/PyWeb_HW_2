from multiprocessing import Pool, cpu_count
import time


def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    return result



if __name__ == '__main__':

    # start_time = time.time()
    # a, b, c, d = factorize(128, 255, 99999, 10651060)
    # end_time = time.time()
    # print("time:", end_time - start_time, "seconds")

    cup_num = cpu_count()
    print(f'cpu_count: {cup_num}')
    k = (128, 255, 99999, 10651060)
    start_time = time.time()
    with Pool(processes=cup_num) as pool:
        pool.map(factorize, k)
        pool.close()
    end_time = time.time()
    print("Parallel version time:", end_time - start_time, "seconds")


