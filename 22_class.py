"""
1.class Keyword
2.instance attributes!
3.class attributes
4.__init__method ->constructor
5.self

"""
class Employee:
    salary=0
    count=0
    def __init__(self): 
        print("In constructor")
        #self.count+=1
        Employee.count+=1

    def getEmployee(self): 
        print("Employee count")
        print(self.count)   #without self we cant use local variable

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.getEmployee()

