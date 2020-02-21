class Employee:
    count=0
    def __init__(self,name,salary):
        print("In constructor")
        self.name=name
        self.salary=salary
        Employee.count+=1

    def getEmployeeDetails(self):
        print("Employee Details:")
        print("Name: ",self.name)
        print("Salary: ",self.salary)

emp1=Employee("obb",88888)
emp2=Employee("aaa",2345)
emp3=Employee("bbb",65433)
emp4=Employee("ccc",432556)

emp1.getEmployeeDetails()
emp2.getEmployeeDetails()
emp3.getEmployeeDetails()
emp4.getEmployeeDetails()

print("team count: ",Employee.count)
print("Access instance attribute directly")
print("emp1 is " + emp1.name +" " +str(emp1.salary))

