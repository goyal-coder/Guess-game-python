import random

computer_generate = random.randint(1, 100)

try:
    user_input = int(input("Welcome to the Guessing Game! 🎮 Guess the number between 1 and 100: "))
    
    while user_input != computer_generate:
        if computer_generate > user_input:
            print("😅 Too low! Come on, shoot higher... you got this!")
        elif user_input > computer_generate:
            print("😜 Whoa there! Too high! Lower your expectations a bit 😉")
        else:
            print("🤔 Hold up! Something’s fishy. You sure you entered a number? Try again!")
        
        user_input = int(input("Guess again... Let's see if you're psychic: "))  
    
    print("🎉 Hurray!! You finally guessed it right! You’re basically a genius now! 🏆")
    
except ValueError:
    print("Oops! 😬 That’s not a number! Come on, give me an integer between 1 and 100, buddy.")
