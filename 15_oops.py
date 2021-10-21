# class Employee: #create class
#     def input(self): #create function
#         username=input("Enter a user name of employee:")
#         eid=int(input("Enter a employee id :"))
        
#         print("user name and id:"+str(username))
#         print("user employee id:"+str(eid))

# emp=Employee() #create class object emp
# emp.input()


#class atributie
# class Employee:
#    company="amazon"
# Akash=Employee()
# print(Akash.company)


#instance atribute
# class Employee:
#     company="amazon"
#     salary="40L"
# Akash=Employee()
# Sakshi=Employee()
# print(Akash.company+"="+Akash.salary)
# Employee.company="google"
# Employee.salary="1C"
# print(Sakshi.company+"="+Sakshi.salary)

# #Self parameter
# class Employee:
#     def getcompny(self):
#         # company="google"
#         company="amazon"
#         return company
# Akash=Employee()
# print(Akash.getcompny())


#Static Method
# class Employee:
# #  n=input("Enter a  company name:")
# #  company=n
# #  def getsalary(self):#unstatic method
# #      salary=input("Enter a salary")
# #      print(f"Your salary this )
# #      return salary
# #  @staticmethod
#  def staticmethod():
#      print("This is static method")

# Akash=Employee() 
# Akash.getsalary()
# Akash.staticmethod()


# #Constructor
# class employee:
#     def __init__(self):
#         name=input("Enter a name:")
#         print("this a constructor function"+name)
#     def username(self):
#         print("This is user function")
#     @staticmethod
#     def staticmethod(self):
#         print("This static method function")

# akash=employee()

# #Problem set
# class Microsoft:
#     def information(self):
#         name=input("Enter a name of Employee:")
#         id=input("Enter a id of Employee:")
#         with open("data.txt",'w') as f:
#             f.write(f"Employee Name:{name} and Employee id:{id}")
# akash=Microsoft()
# akash.information()


# class train:
#     def ticket(self):
#         tic=input("Enter a ticket")
#         t=[tic]
#         with open("data.txt",'w') as f:
#          f.write(tic)
#         return t
#     def status(self):
#         s=input("Enter a ticket number")
#         with open("data.txt",'r') as r:
#          data=r.read()
#         if s in data:
#             print("seat is aviable")
#         else:
#             print("set is not avaiable")
#     # def infotrain:
#     #     pass
        
# akash=train()
# akash.ticket()
# akash.status()


  