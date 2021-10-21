import random
randnumber=random.randint(1,100)
print(randnumber)
userguess=None
guesses=0
while(userguess != randnumber):

 userguess=int(input("Enter your guess:"))
 guesses+=1
 if userguess==randnumber:
    print("Your guess is right")
 else:
    if(userguess>randnumber):
       print("Your guess is wrong!Enter a small number")
    else:
       print("Your guess is wrong!Enter a Larger nmuber")
print(f"your guessed the number in {guesses}guesses")
with open("data.txt",'w') as f:
    guesses=str(guesses)
    f.write(f"Your guesses is:{guesses}")