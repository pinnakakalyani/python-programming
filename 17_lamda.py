'''
no name or anaonymous function
'''
def addmun(n1,n2):
    return n1+n2
sum=addmun(4,4)
print(sum)

#lamda way
sum=lambda n1,n2:n1+n2
print(sum(3,7))

#lamda way
message=lambda m:print(m)
print(message("hello lamda"))

squared=lambda n:n*n
print(squared(5))

#list of lambda functions (function in collection)
lambdalist=[lambda a:a*2,lambda a,b:a*2,lambda a,b:a+b]
print(lambdalist[0](8))
print(lambdalist[1](4,8))
print(lambdalist[2](5,6))

#lambda with no parameters
noparam=lambda: True # lambda should not be empty it should return something
print(noparam())
