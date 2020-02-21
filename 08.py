#lists
mixed=[2,4,8,"kalyani",88.88,1,43,"venky",'l']
print(mixed[4])
print(id(mixed))
#:operator
print(mixed[3:8])
#Sclice from 3rd index position to (8-1)th position
newslice=mixed[3:8]
print(type(newslice))
#slice from negative direction
backslice=mixed[-4:-1]
print(backslice)

backslice1=mixed[-5:]
backslice2=mixed[-5::1]
print(backslice1)
print(backslice2)


#iterating through the list!
for item in mixed:
    print(item)

providers={"uber","ola","zoom","ridzer","didi"}
firstproviders=[provider[0] for provider in providers]
print(firstproviders)
lengthofEachItem=[len(provider) for provider in providers]
print(lengthofEachItem)
print("uber" in  providers)
print('l' in "kalyani")

# add items to list
getx=[x+y for x in 'abc' for y in 'def']
print(getx)

#creating 2 dimensional list
print("abc" * 4)
clone=[4]*3
print(clone)
'''
    [4,4,4],
    [4,4,4],
    [4,4,4]
'''
clone2=[[4]*3]*3
print(clone2)

#list additions
friends1=["oma","oka","chia"]
friends2=["pic","Din","aaa"]
friends3=friends1+friends2
print(friends3)

print(mixed)
print(mixed[0: 7: 3])

mixed.insert(0,55)
print(mixed)
check=mixed.pop(0)
print(str(check) + " popped of " + str(mixed))
print(mixed)
print(mixed.pop()) #delete last element


#create 2 dimensional list using for
'''
[4]*3 ->range(0,2)
'''
twodimension=[[4]*3 for a in range(0,3)]
print(twodimension)


twodimension1=[[a]*3 for a in range(0,3)]
print(twodimension1)

twodimension2=[[a*a]*3 for a in range(0,3)]
print(twodimension2)

twodimension2=[[a**(a+1)]*3 for a in range(0,3)]
print(twodimension2)
