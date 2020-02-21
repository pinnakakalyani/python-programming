class Employee:

    def __init__(self,fname,lname):
        print("Employee constructor")
        self.fname=fname
        self.lname=lname

    def getfname(self):
        return self.fname

    def getlname(self):
        return self.lname  

    def getEmployeeDetails(self):
        print("In getEmployee details") 

class FullstackEngineer(Employee):
    def __init__(self, fname, lname,tech):
        self.tech=tech
        super().__init__(fname,lname)

    def getEmployeeDetails(self):
        return "Name: " +self.fname+" "+self.lname+"\n" + "Technology :" +self.tech

fse1=FullstackEngineer("assa","azds","java")
print(fse1.getEmployeeDetails())
print(fse1.getfname())
print(fse1.getlname())

emp1=Employee("adsd","feew")
emp1.getEmployeeDetails()
        
