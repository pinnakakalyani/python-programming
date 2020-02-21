import threading
import time

def getSquare(numList):
    print("calculate square of numbers")
    for n in numList:
        print("square: " ,n*n)



def getCube(numList):
    print("calculate cube of numbers")
    for n in numList:
        #time.sleep(1)
        print("cube: " ,n*n*n)      

numbers = [1,2,3,4,5,6,7,8] 
#Single threaded execution!
t=time.time()
print('{:-^80}'.format("Single threaded execution"))
getCube(numbers)
getSquare(numbers)
print("Time to execute is: ",time.time() - t)

t=time.time()
print('{:-^80}'.format("Multi threaded execution"))
thread1=threading.Thread(target=getSquare,args=(numbers,))
thread2=threading.Thread(target=getCube,args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Time to execute is: ",time.time() - t)
print("Done with Maths Exhasted now!")