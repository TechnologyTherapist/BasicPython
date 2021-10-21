import random#its used random value
def game(com,you):
 if com==you:
    return None
 elif com =='s':
     if you=='w':
         return False
     elif you=='g':
         return True
 elif com =='w':
     if you=='g':
         return False
     elif you=='s':
         return True
 elif com =='g':
     if you=='s':
         return False
     elif you=='w':
         return True





print("Comp Turn:Snake(s) Water(w) Gun(g)")
randno=random.randint(1,3)
if(randno==1):
    com='s'
elif(randno==2):
    com='w'
elif(randno==3):
    com='g'
you=input("Your Turn Select:Snake(s) Water(w) Gun(g)")
a=game(com,you)
print(f"Computer Choose:{com}")
print(f"Your Choose:{you}")
if a==None:
    print("Match is Draw")
elif a:
    print("you win")
else:
    print("you Lose")