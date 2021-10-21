class number:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,num2):
        print("This Constructor to perform addition")
        return self.num+num2.num
    def __mul__(self,num2):
        print("This constructor perform multipilation ")
        return self.num*num2.num
    def __str__(self):
        return f"This Decimal number:{self.num}"
    def __len__(self):
        return 1
n1=number(int(input("Enter a number n1:")))
n2=number(int(input("Enter a number n2:")))
sum=n1+n2
mul=n1*n2

print(sum)
print(mul)
n3=number(int(input("Enter a number :")))
print(n3)
print(len(n3))