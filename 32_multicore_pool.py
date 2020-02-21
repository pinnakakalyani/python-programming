from multiprocessing import Pool
import time

def myfunction(numList):
    counter=0
    for i in range(1000):
        counter=i*i
    return counter

if __name__ == "__main__":
    t1=time.time()
    pool= Pool()
    result=pool.map(myfunction,range(100))
    pool.close()
    pool.join()

    print("Time taken by pool: ",time.time()-t1)

    t2=time.time()
    for i in range(10000):
        result.append(myfunction(i))

    print("Time taken by serial processing: ",time.time()-t1)