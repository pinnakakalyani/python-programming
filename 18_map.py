#map will only work on iterables!
#it will return the list created by lambda function
# lambda function works on parameter of map

message=['Help','run','fight','request']

for m in message:
    print("current mesasage is : ",m)

def printmessage(mssg):
    return "message from function is " +mssg

mapcheck=map(printmessage,message)
print(list(mapcheck))

#working with map and lambda
mapcheck=map(lambda m:"lambda map" +m, message)
print(id(mapcheck))
newlist=list(mapcheck)
print(type(list(mapcheck)))
print(id(mapcheck))
print(newlist)
print(list(mapcheck))

#mapcheck is becoming empty list after type check as list constructor is being used

scores1=[25,35,45]
scores2=[10,15,20]
scores3=[2,3,4,5]
#scores1 and scores2
scores3=map(lambda n1,n2,n3:(n1+n2)*n3,scores1,scores2,scores3)
print(list(scores3))

#considering senario with list of different length
scores1=[25,35,45,56,78]
scores2=[10,15,20,30]
scores3=[2,3,4,5]

#scores3=sum of each respective item at respective index position at scorea1 and scores2

scores3=map(lambda n1,n2,n3:(n1+n2)*n3,scores1,scores2,scores3)
print(list(scores3))


