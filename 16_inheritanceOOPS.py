#Single Inheritance
# class Employee:
#         # name='Akash'
#         # age=20
#         # Salary=100000
        
#         name=input("Enter a Employe Name:")
#         age=input("Enter a employee age:")
#         Salary=input("Enter a Employee salary:")

# class Company(Employee):
#     def Display(self):
#         print( f"Emplyee Name Is :{self.name}")
#         print(f"Employee age is :{self.age}")
#         print(f"Employee salary is:{self.Salary}")
# e=Employee()
# c=Company()
# c.Display()


# #Multiple Inheritance
# class Student:
#     def StuInfo(self):
#         name=input("Enter a Student Name:")
#         rollno=input("Enter a Roll No:")
#         print(f"Student Name Is:{name}")
#         print(f"Student Rollno Is:{rollno}")
# class Treacher:
#     def marks(slef):
#         num=input("Enter a Marks :")
#         print(f'Students Marks is:{num}') 
# class parents(Student,Treacher):
#     def result(self):
#      print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<This Your Resulat >>>>>>>>>>>>>>>>>>>>>>>>>>>")
# s=Student()
# t=Treacher()
# p=parents()

# p.StuInfo()
# p.marks()
# p.result()


# #Multilevel Inheritance
# class Parentclass:
#     n=input("Tpye ANything Okay:")
#     def parentmethod(self):
#         print("This is Parent Method")
# class child1(Parentclass):
#     def childmethod1(self):
#         print(f"This is Child Method 1:")
# class Child2(child1):
#     def childmethod2(self):
#         print("This is Child Method 2:\n")
#         print(f"This Statement Print Parent Class Attributes:"
#         )
# pr=Parentclass()
# c1=child1()
# c2=Child2()
# c2.childmethod1()
# c1.parentmethod()

# # Super Method
# class Derived2:
#     def __init__(self):
#         n=print("This is a Constructor ")
#     n=input("Hii Your are in Second Derived Class Now Enter a Any Statement:")
#     d2=print(n)
#     def derived2(self):
#         print("This is a Second Derived Class")
# class Derived(Derived2):
#     n=input("Enter a any Statement:")
#     d=print(f"This derived class attributes:{n}")
#     def derived(self):
#         super().__init__()
#         super().derived2()
#         print("This is a  Derived Class")
# class Base(Derived):
#     def base(self):
#         super().derived()#This super method call Derived Function And Print a data
#         print("This is a base class")
# b=Derived()
# b.derived()

# #Class Method
# class Employee:
#     name=input("Enter a name:")
#     # salary=int(input("Enter A Salary"))
#     location=input("Enter a Location")
#     Name=name
#     Salary=1234
#     Location=location
#     @classmethod
#     def changeslary(cls,sal):#Change the value of attributes  inn class  example salary using  classMethod
#         cls.Salary=sal
# e=Employee()
# e.changeslary(4321)
# print(e.Salary)
# print(Employee.Salary)

#Property Method
class account:
    salary1=int(input("Enter a One Salary your:"))
    salary2=int(input("Enter a Second Salary Your:"))
    @property
    def totalsalary(self):
        return self.salary1+self.salary2

    @totalsalary.setter
    def totalsalary(self,val):
     self.salary1=val-self.salary2
     self.salary2=val-self.salary1
    #  print(salary1)
    #  print(salary2)
a=account()
print(a.totalsalary)
a.totalsalary=1000
print(a.salary1)
print(a.salary2)

