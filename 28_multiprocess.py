import time
import multiprocessing

result=[]

def getsquare(numlist,resc):
    for n in numlist:
        time.sleep(4)
        resc.append(n*n)
        print("square:",n*n)
    print(resc)
print(result)

'''def getcube(numlist):
    for n in numlist:
        time.sleep(4)
        print("Cube: ",n*n*n)'''

if __name__ == '__main__':

    numbers=[1,2,3,4,5]

    process1=multiprocessing.Process(target=getsquare,args=(numbers,result))
   # process2=multiprocessing.Process(target=getcube,args=(numbers,))

    process1.start()
    #process2.start()

    process1.join()
    #process2.join()

    print("Done with Multiprocessing!")

