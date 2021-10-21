# def per(marks):
#     p=(sum(marks)/400)*100
#     return p
# marks1=[10,20,60,80]
# marks1=per(marks1)
# marks2=[40,50,60,70]
# marks2=per(marks2)
# print(marks1,marks2)

# def user():
#     n=input("Enetr a your name:")
#     print("Good Day:"+n)
#     return n
# user()

# def sum1(a,b):
#     c=a+b
#     print("Addition of two number is :"+str(c))
#     return c

# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number :"))
# sum1(n1,n2)


# def fac():
#    r=int(input("Enter a number"))
#    product=1
#    for i in range(r):
#     product=product * (i+1)
#     print(product)
# fac()

# def fac_recursion(n): #Recursion logic used
#     if n==1 or n==0:
#      return 1
#     return n*fac_recursion(n-1)
  
# f=fac_recursion(4)
# print(f)

#Problem Set
#WAP thre largest number
# def larg():
#     n1=int(input("Enter a number :"))
#     n2=int(input("Enter a number :"))
#     n3=int(input("Enter a number :"))
#     if(n1>n2 and n1>n3):
#         print("this is number is largest:"+str(n1))
#     elif(n2>n1 and n2>n3):
#        print("This is number is Largest:"+str(n2))
#     else:
#         print("This is number is largest:"+str(n3))
# larg()

# def cel_fahren():
#     c=int(input("Enter Celsius Value:"))
#     F=c*(9/5)+32
#     print("Celsius Convert Fahrenheit="+str(F))

# cel_fahren()


# def sum_recursion(n):
#   if(n!=0):
#       return n+sum_recursion(n-1)
#   else:
#       return n 
# num=int(input("Enter a positive integer"))


# def star(n):
#   for i in range(n):
#    print("*"*(n-i))

# num=int(input("Enter a number:"))
# star(num)     

# def remove_strip(str,word):
#     newstr=str.replace(word,"")
#     return newstr.strip()

# string=input("Enter a String:")
# string2=input("Enter a word to remove:")
# n=remove_strip(string,string2)
# print(str(n))
      

# def multi_table(n):
#  for i in range(10):
#      print(str(n)+"*"+str(i+1)+"="+str(n*(i+1)))

# num=int(input("Enter a table number :"))
# multi_table(num)