from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculatesalary(self):
        pass
class HourlyEmployee(Employee):
    def __init__(self,name,perhrsalary,totalhours):
        self.name=name
        self.perhrsalary=perhrsalary
        self.totalhours=totalhours
        
    def calculatesalary(self):
        cal=self.perhrsalary*self.totalhours
        print("total calculated salary of "+self.name+" is "+str(cal))
class SalariedEmployee(Employee):
    def __init__(self,name,monthly_salary,allowance):
        self.name=name
        self.monthly_salary=monthly_salary
        self.allowance=allowance
    def calculatesalary(self):
        cal=self.monthly_salary+self.allowance
        print("total calculated salary of "+self.name+" is "+str(cal))
class Manager(Employee):
    def __init__(self,name,base_salary,bonus):
        self.name=name
        self.base_salary=base_salary
        self.bonus=bonus
    def return_salary(self):
        return self.base_salary
    def calculatesalary(self):
        cal=self.base_salary+2*self.bonus
        print("total calculated salary of "+self.name+" is "+str(cal))
class Executive(Employee):
    def __init__(self,name,base_salary,experience):
        self.name=name
        self.base_salary=base_salary
        self.experience=experience
    def calculatesalary(self):
        cal=self.base_salary+4*self.experience
        print("total calculated salary of "+self.name+" is "+str(cal))
class Company():
    def __init__(self,base_salary):
        self.base_salary=base_salary
        
    def HireEmp(self):
        eh_no=input("enter no of employees to be hired:")
        print("enter details of employee to be hired:")
        for i in range(int(eh_no)):
            e_name=input('enter emp name:')
            e_desig=input("enter emp desig:")

            fh=open(r"C:\Users\user\Desktop\abc.txt",'a')
            fh.write(e_name+"\t   ")
            fh.write(e_desig)
            fh.write("\n")
            fh.close()
        print(eh_no+" employee(s) is/are hired")
    def FireEmp(self):
        ef_no=int(input('enter no of employees to be fired:'))
        for i in range(int(ef_no)):
            ef_name=input('enter name of emp to be fired:')
            fh=open(r"C:\Users\user\Desktop\abc.txt","r")
            lines=fh.readlines()
            fh=open(r"C:\Users\user\Desktop\abc.txt","w")
            for line in lines:
                if ef_name not in line:
                        fh.write(line)
            fh.close()
        print(str(ef_no)+" employee(s) is/are fired")   
    def raise_emp_sal(self,object1):
        #object1 here want to take object of manager class        salary = object1.return_salary()
        name=input('enter name of employee whose salary has to be raised:')
        salary=self.base_salary+0.1*self.base_salary
        print('salary of employee '+name+' is raised to '+str(salary))
        
H_E=HourlyEmployee("rahul",25,360)
H_E.calculatesalary()
S_E=SalariedEmployee("vishal",30000,250)
S_E.calculatesalary()
man=Manager("abc",40000,500)
man.calculatesalary()
man.return_salary()
ex=Executive("pqr",50000,4)
ex.calculatesalary()
com= Company(30000)       
print("enter 1 to hire emp")
print("enter 2 to fire emp")
print("enter 3 to raise emp salary")
while True:
    choice=int(input("enter your choice:"))    
    if choice==1:
        com.HireEmp()
    elif choice==2:
        com.FireEmp()
    elif choice==3:
        com.raise_emp_sal(man)
    else:
        break
     
