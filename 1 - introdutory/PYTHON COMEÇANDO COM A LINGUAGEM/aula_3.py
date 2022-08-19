import random

print("Guess the number! Type a number and try finding the secret number.")

secret_num = random.randint(1,100)

guess = int(input("Type a number: "))


def guessNumber(guess):
    if guess == secret_num:
        print(f"You typed {guess} and got the correct secret number!")
        print("Congratulations!")
        return  
    elif guess > secret_num:
        print(f"You typed {guess}, but it is an incorrect answer. Try something smaller")
        guess = int(input("Type a number: "))
        guessNumber(guess)    
    elif guess < secret_num:
        print(f"You typed {guess}, but it is an incorrect answer. Try something bigger")
        guess = int(input("Type a number: "))
        guessNumber(guess)

guessNumber(guess)