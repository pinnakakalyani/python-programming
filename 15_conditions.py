'''
if expression :
    pass
if condition:
    pass
else:
    pass
'''
number=int(input("Input number:"))
if(number>30):
    print("number is more than 30")
else:
    print("something else")

numbers=[1,2,3,4,5,6,7,8,9]
number=int(input("input number: "))

if(number in numbers ):
    print("yes")
else:
    print("No")

friends1={"ola","uber","didi","mave","ride"}
friends2={"ride","jia","kiki","zoom"}

for f in friends1:
    if f in friends2:
        print("common friends:",f)
    """else:
        print("no friends")"""
