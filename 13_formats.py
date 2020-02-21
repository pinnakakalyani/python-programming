#{}.format(parameter)
# print("format the string")

print("{}".format("format the string"))

fname="prafful"
lname="daga"
print("{}....{}".format(fname,lname))

#use format to alignand give width of output

print(format(fname,">50s"))
print(format(fname,"<50s"))

#fill empty spaces with any character
print(format(fname,"#<50s"))
print(format(fname,"$>50s"))
print(format(fname,"@^50s"))

#use integers with format strings
print("score is {}".format(8))
print("score is {}".format(8888))
print("score is {:,}".format(888888))
print("score is {:15,}".format(888888888))
print("score is {:-<15,}".format(88888888))
print("score is {:->15,}".format(88888888))
print("score is {:-^15,}".format(88888888))

#integer to binary
number=10
print("Binary of {0} is {1:b}".format(number,number))

number=0
while(number<=15):
    print("Binary of {0} is {1:b} octal: {2:o} Hexadec: {3:x}".format(number,number,number,number))
    number+=1

#use format to access list and dictionary items!
language=['python','django','java','node']
print("I love to work with {}".format(language))
print("I love to work with {0[1]}".format(language))

friends={"mohan":"chennai","yuko":"japan"}
print("Mohan is from {0[mohan]} \nyuko is from {0[yuko]}".format(friends))



