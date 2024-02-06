"""Number Guessing Game."""
from random import randint

SECRET : int= randint(1,5)
correct: bool= False
print("Hi. Lets play a guessing game!!")
while correct== False:
    guess: int= int(input("Guess a number: "))
    if guess >= 6:
        print("Guess is greater than 5")
        print("Guess Again: ")
    elif guess <= 0:
        print("Guess is lesser than 1")
        print("Guess Again: ")
    else:    
        if guess== SECRET:
            print(f"Correct! {guess} is the number")
            correct= True
        elif guess >= SECRET:
            print("Guess is too high")
        else: 
            print("guess is too low")
        

 # store your emoji string for a singular row.
user_col == col_count: