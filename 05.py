#integer
n1=5
print(str(n1) + " is type of " + str(type(n1)))

#float
n2=5.5
print(str(n2) + " is type of " + str(type(n2)))


#lists
mixed=[]
print(type(mixed))
mixed=[2,5.5,'a','b',"uber"]
print(type(mixed))
print(mixed)
print(mixed[0])
print("length of list is" + str(len(mixed)))


#tuple
nochange=()
print(type(nochange))
nochange=(2,2.5,'a','b',"asd")
print(nochange)
print(nochange[0])
#below stmt is illegal for tuple
#nochange[0]=4


#strings
location="chennai"
multiline= '''
            "hello" +" how "+
            "are " +"you"

            '''
print("location:"+ str(type(location)))
print(len(location))
print(location[0])
print(multiline)

#sets
noorder={25,35,45,65}
print(type(noorder))
print(noorder)
#print(noorder[0])

#dictionary
keyvalue={}
print(type(keyvalue))
keyvalue={ 1:"kalyani","tech":"python", 4:8,9:"ML"}
print(keyvalue[1])
print(keyvalue["tech"])
print(keyvalue[4])
print(keyvalue[9])

#type conversion
n2=5
print(type(n2))
n3=float(n2)
print(type(n3))
n4=str(n3)
print(type(n4))

#input
score1=input("Input Score 1:")
score2=input("Input Score 2:")
print("Score is :" +score1+score2)
print("########################")
score1=int(input("Input Score 1:"))
score2=int(input("Input Score 2:"))

print("Score is : " +str(score1+score2))
print("Score is ",score1)
