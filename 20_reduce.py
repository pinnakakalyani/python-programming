"""
Reduce -> Aggregate functions!

1.It works with iterable
2.it will return single value
"""

from functools import reduce

numbers=[1,2,3,4,5]
total=reduce(lambda n1,n2: n1+n2,numbers)
print(total)

numbers=[55,45,65,75,85,95,35,25]
largest=reduce(lambda a,b:a if a>b else b , numbers)
print(largest)

smallest=reduce(lambda a,b:a if a<b else b , numbers)
print(smallest)

numbers=[5,15,10,8,2,3,6,18,7]
#numbers=[5,6,11]
#25+36
#61
#sum of square of all lessthan 10

total=reduce(lambda a,b:a+b,map(lambda a:a*a ,filter(lambda n :n<10, numbers)))
print(total)

def add(a,b):
    return a+b

def mul(c):
    return c*c

def less(d):
    if d<10:
        return True
    else:
        return False

sum1=reduce(add,map(mul,filter(less,numbers)))
print(sum1)


square=reduce(lambda a,b:a+b, map(lambda a:a*a,filter(lambda n:n%2==0,numbers)))
print(square)