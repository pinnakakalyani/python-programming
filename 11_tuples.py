sample=()
print(type(sample))
sample=25,65,45
sample=(25,65,45,[90,"check",5.5])
print(sample)
sample=((3,4,5),(7,8,9),(1,9,0))
print(sample)
print(sample[1][1])

#creating tuples from lista and sets
scores=[25,35,45]
sample=tuple(scores)
print(sample)

scores={25,35,45}
sample=tuple(scores)
print(sample)

onlyOne='omg'
#checkone=tuple(onlyOne)
checkone=(onlyOne,)
print(checkone)
print(type(checkone))

sample=(25,65,45,[90,"check",5.5],34,45,55)
print(sample[0:5])
print(sample[0:])
print(sample[:5:3])

#tuple is immutable ->you cannot modify element to insert tuple but can assign a new tuple to same variable

sample=(25,35,65)
print(sample[0])
#TypeError:'tuple' object does not support item assignment
#sample[0]=33
sample=(44,85,45)
print(sample)
vovel1=('a','e','i')
vovel2=('o','u')
vovel=vovel1+vovel2
print(vovel)

#delete is not possible in tuple
del  vovel
