import time
import multiprocessing

result=[]

def getsquare(numlist,resc):
    print(numlist)
    print(resc)
    for index, n in enumerate(numlist):
        print(index," ",n)
        resc[index]=n*n
    print("Result in process1: ",list(resc))

if __name__ == '__main__':

    numbers=[1,2,3,4,5]

    result=multiprocessing.Array('i',5)
    score=multiprocessing.Value('d',0.0)
    process1=multiprocessing.Process(target=getsquare,args=(numbers,result))
  
    process1.start()

    process1.join()
    
    print("Result list in process1: ",list(result))

    print("Done with Multiprocessing!")

