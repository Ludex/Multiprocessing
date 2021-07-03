from math import ceil, sqrt
import multiprocessing
import time

#Sequential
def check_prime(N):
    arr = [True]*N
    for num in range(N):
        if num < 2:
            arr[num] = False
        elif num == 2:
            arr[num] = True
        else:
            for j in range(2, ceil(sqrt(num))+1):
                if num%j==0:
                    arr[num] = False
                    break
    return arr

def check_prime_multi(num):
    if num < 2:
        #return num, False
        return False
    elif num == 2:
        #return num, True
        return True
    else:
        for j in range(2, ceil(sqrt(num))+1):
            if num%j==0:
                #return num, False
                return False
    #return num, True
    return True

if __name__ == '__main__':
    N = 2 * 10**6

    #Single-processing
    st = time.time()
    results = check_prime(N)
    en = time.time()
    print(results[:30])
    print(f'Time taken: {en-st}')

    #Multi-processing
    st = time.time()
    num_array = range(N)
    num_processes = 10
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(check_prime_multi, num_array)
    #pool.close()
    en = time.time()
    print(results[:30])
    print(f'Time taken: {en-st}')