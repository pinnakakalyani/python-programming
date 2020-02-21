'''def funcname(parameter_list):
    pass
'''
counter=10
def custommssg(message):
    global counter
    if(counter>0):
        print(message)
        counter-=1
        custommssg(message)

custommssg("Hello!")



def addnumbers(number1,number2):
    global sum
    while(number1<number2):
        sum=number1+1
        print(sum)
        if(sum>number2):
            return sum
        number1=sum
number1=int(input("start number"))
number2=int(input("end number"))
sum=0
addnumbers(number1,number2)           
