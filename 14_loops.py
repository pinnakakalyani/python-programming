'''for loops'''
vowel="aeiou"

for v in vowel:
    print(v)

numbers=[1,2,3,4,5,6,7,8,9,0]
total=0
for n in numbers:
    #total =total+n
    print("sum of all list from 1 to 10 ", total)

#using from loop with range
for n in range(1,5):
    print(n,end=" ")
print()
for n in range(1,10,2):
    print(n, end=" ")

#in below case else will not execute as loop is breaking in between
for n in numbers:
    print(n**n)
    if(n==7):
        break 
else:
    print("Exponent for all numbers is done")    




