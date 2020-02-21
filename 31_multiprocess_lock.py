import multiprocessing
import time

def depositMoney(money,lock):
    for i in range(4000):
        lock.acquire()
        money.value +=1
        lock.release()
        print("deposit ", money.value())

def withdrawMoney(money,lock):
    for i in range(4000):
        lock.acquire()
        money.value -=1
        lock.release()
        print("Withdraw ", money.value())

if __name__ == "__main__":
    lockprocess=multiprocessing.Lock()
    balanceMoney=multiprocessing.Value('i',0)
    process1=multiprocessing.Process(target=depositMoney,args=(balanceMoney,lockprocess))
    process2=multiprocessing.Process(target=withdrawMoney,args=(balanceMoney,lockprocess))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Final Balance :" ,balanceMoney.value())


