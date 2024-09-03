#NUMBER GUESSING GAME!!

import random

Cptr_no = random.randrange(1,100)                           #Computer will select a number for guess!!
u_guess_no = int(input("Guess the number between 1 to 100 : "))        #User will guess the number!!

while u_guess_no != Cptr_no:
    if u_guess_no > Cptr_no:
        print("Try Again !! \n Your guess is too high :(")
    else:
        print("Try Again !! \n Your guess is too low :(")
    u_guess_no = int(input("Enter your number between 1 to 100 : "))

print("Yeahhh!! Your guess is correct and you won !!", Cptr_no)


