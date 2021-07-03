import multiprocessing
import time

def counter1(num):
    cnt = 0
    for i in range(num):
        cnt += 1
    print("Counter 1 done!")

def counter2(num):
    cnt = 0
    for i in range(0, num, 2):
        cnt += 1
    print("Counter 2 done!")

if __name__ == "__main__":
    N = 2 * 10**8

    #Single processing
    st = time.time()
    counter1(N)
    counter2(N)
    en = time.time()
    print(f"Time taken: {(en-st):.2f}")

    #Multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=counter1, args=(N,))
    p2 = multiprocessing.Process(target=counter2, args=(N,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    en = time.time()
    print(f"Time taken: {(en-st):.2f}")