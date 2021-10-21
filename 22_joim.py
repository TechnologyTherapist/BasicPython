# # # list1=['akash','sakshi']
# # # satance='\n'.join(list1)
# # # print(satance)



# # #Format method using
# # a=input("Enter a String Please:")
# # string="Hello guys my name is {}".format(a)
# # print(string)

# # # Map Filter and reduce
# # def sum(num):
# #     return num+num
# # list1=[1,2,3,4]
# # # list2=[]
# # # for item in list1:
# # #     list2.append(sum(item))
# # # print(list2)
# # print(list(map(sum,list1)))


# # Filter Method()
# def lessthan(self):
#     if self<10:
#         return True
#     else:
#         return False
# greaterthan=lambda self:self>10
# list1=[1,23,4,5,6,7,89,0]
# print(list(filter(lessthan,list1)))
# print(list(filter(greaterthan,list1)))
       

# # # Reduce Funtion()
# from functools import reduce
# list1=[1,23,4,5]
# sum=lambda a,b:a+b
# a=reduce(sum,list1)
# print(a)

# Problem set
# name=input("Enter a your name please:")
# marks=int(input("Enter your marks:"))
# phonenumber=int(input("Enter a your phone number"))
# string='The name of the student is {0},his marks are {1} and phone number is {2}'.format(name,marks,phonenumber)
# print(string)

# table=[str(i*7) for i in range(1,11) ]
# print(table)
# table7= '\n'.join(table)
# print(table7)

# list1=[10,5,15,65,7,454,66,436,3,6543,3,3,65,6,25]
# dev=lambda num:num%5==0
# print(list(filter(dev,list1)))

from functools import reduce
list1=[12,32,3343,5,6,567,687,8,79,89]
# def graterthan(a,b):
#     if a>b:
#         print(f"This is number larger:{a}")
#     elif b>a:
#         print(f"This number larger:{b}")
#     else:
#         return False
large=reduce(max,list1)
print(large)

