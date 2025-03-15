# Guess the Number Game Python Project (computer)
# In this Kylie Ying tutorial, you will learn how to work with Python's random module, build functions, work with 
# while loops and conditionals, and get user input

import random

def guess_number():
    print("\nwelcome to the guessing number game:\n")
    number = random.randint(1,100)
    guess_left = 5

    while guess_left > 0 :
        print(f"you have {guess_left} guesses left:") 
        try:
            guess =  int(input("Enter the guess number:"))
        except ValueError:
            print("invalid number:\n Enter the number")
            continue
        if(number>guess):
            print("low value")
        elif(number<guess):
            print("high value")  
        else:
            print(f"Congratulations! You guessed the number")
            return
        guess_left -= 1 
    
    print(f"\nYou ran out of guesses. The number was {number}.")


if __name__ == "__main__":
    guess_number()
























