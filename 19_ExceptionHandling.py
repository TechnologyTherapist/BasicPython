# # while(True):
# #     print("if you exit this code press q")
# #     a=input("Enter a Number:")
# #     if a=='q':
# #         break
# #     try:
# #       a=int(a)
# #       if a>10:
# #         print(f"Your number is greater than 10:{a}")
# #       else:
# #         print(f"Your number is Less than 10:{a}")
# #     except Exception as e:
# #      print(f"This your error:-{e}")
# # print("This is code is correct")

# # ####Example of tpyes of Exception
# # n=int(input("Enter a value:"))
# # try:
# #   ans=1/n
# #   print(ans)
# # except ValueError as e:
# #   print(f"This error to your code:{e}")
# # except ZeroDivisionError as e:
# #   print(f"Check Yuor number:{e}")
# # print("//////////////////////////////This cose we run |||||||||||||||||||||||||")

# # # Custom Exception message
# # def decreament(num):
# #   try:
# #     num=int(num)
# #     return num-1
# #   except:
# #     raise  ValueError("This not goog")
# # a=decreament('aka')
# # print(a)


# # #try with else clause
# # try:
# #    a=int(input("Enter a number:"))
# #    ans=1/a
# #    print(a)
# # except Exception as e:
# #   print(f"Please check your value:{e}")
# # else:
# #   print("Your code run")


# # # try with finally
# # try:
# #  n=int(input("Enter a  number:"))
# #  if n/2:
# #   print(f"This even number:{n}")
# #  else:
# #   print(f"This is odd number:{n}")
# #   exit()
# # except Exception as e:
# #   print(f"this is your error:{e}")
# # finally:
# #   print("Will try again")
# # print("Your answer is Crrorect")

# # # global and locals variable
# # a=10#Global variable
# # def fun():
# #   global a
# #   a=4#Local variable used global keyword to change local to global
# #   print(a)
# # fun()
# # print(a)


# # # enumerate
# # list1=['akash','sakshi','i','love','you']
# # # index=0
# # # for item in list1:
# # #   print(item,index)
# # #   index+=1
# # # for index,type in enumerate(list1):
# # #   print(index,type)


# # List comprehension
# # list1=[2,4,6,8,1,2,3,4,5,6,7,7,8,9,0,9,9,67,5,4,23,1,2,1,2,342,45,5,46,5,7,67,638,78,74,89,7566,25,45,4,65,7,4526,5,62,6,52,26]
# # # list2=[]
# # # for item in list1:
# # #   if item%2==0:
# # #     list2.append(item)
# # #     print(list2)
# # list2=[item for item in list1 if item%2==0]
# # print(list2)


# ################################=Problem Set=#########################################################
# # try:
# #   n=input("Enter a file name :")
# #   with open(n,'r') as r:
# #     data=r.read()
# #     print(data)

# # except Exception as e:
# #     print(f"your file error{e}")

# list1 = ['akash', 'ak', 2, 44, 88, 99, 00, 69, 'ak47', 'sk']
# # lsit2=[]
# # item=list1
# for index, item in enumerate(list1):
#     n = int(input("Enter a position number:"))

#     if index == n-1:
#         print(f"The {index+1} the element is:{item}")

# num=int(input("Enter a table number:"))
# table=[num*i for i in range(1,11)]
# print(table)

# def div():

#     a = int(input("Enter a number a:"))
#     b = int(input("Enter a  number b:"))
#     try:

#         c = a/b
#         print(f"This your answer:{c}")
#     # except ZeroDivisionError as e:
#     #     print(f"Check your number error {e}")
#     except:
#         raise ZeroDivisionError("Infinite")


# div()

num=int(input("Enter a  number to genrate table:"))
table=[num*i for i in range(1,11)]
with open('table.txt','a') as w:
  w.write(str(table))
  w.write('\n')