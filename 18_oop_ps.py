# #problem set
# class c2dvec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j"
# class c3ddev(c2dvec):
#     def __init__(self,i,j,k):
#         super().__init__(i, j)
#         self.kcap=k
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

# v2d=c2dvec(4,8)
# v3d=c3ddev(1,2,3)
# print(v2d)
# print(v3d)

# class animal:
#     pass
# class pets:
#     pass
# class dog:
#   @staticmethod
#   def brak():
#       print("how is dog a bow bow!")
# b=dog()
# b.brak()


# class employee:
#     # def addsalary(self):
#     salary=int(input("Enter a Salary Employee"))
#     @property
#     def changesalary(self):
#         increment=int(input("Enter a value to increment of salary"))
#         return self.salary*increment
#     @changesalary.setter
#     def changesalary(self,val):
#         self.increment=val/self.salary
# e=employee()
# print(e.changesalary)
# print(e.increment)

class Vector:
    def __init__(self,vac):
        self.vac=vac
    def __str__(self):
        str1= " "
        index=0
        for i in  self.vac:
            str1 +=f"{i}a{index}+"
            index +=1
        return str1[:-1]
    def __add__(self,vac2):
        if len(self.vac)==len(vac2):
         newlist=[]
         for i in range(len(self.vac)):
            newlist.append(self.vac[i] + vac2.vac[i])
         print("Code is run")
         return Vector(newlist)
        else:
            print("Length is not same")
    def __mul__(self,vac2):
        sum=0
        if len(self.vac)==len(vac2):
            for i in range(len(self.vac)):
             sum +=self.vac[i]*vac2.vac[i]
            print("Code is Currect")
            return sum
        else:
            print("Code is wrong")           
    def __len__(self):
        return len(self.vac)
v1=Vector([1,2,4,4])
v2=Vector([4,3,4,4])
print(v1+v2)
print(v1*v2)
# print(len(v1))

# class Vector:
#     def __init__(self,vac):
#         self.vac=vac
#     def __str__(self):
#         return f"{self.vac[0]}i+{self.vac[1]}j+{self.vac[2]}k"

# v1=Vector([1,2,3,4])
# print(v1)

        