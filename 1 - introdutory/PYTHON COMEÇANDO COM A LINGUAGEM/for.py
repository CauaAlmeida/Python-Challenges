import random

secret_num = random.randint(1, 10)
attempts = 10
turn = 1

print("Guess the number! Type a number and try finding the secret number.")
print(f"You have {attempts} attempts")
guess = int(input(f"[Turn nº{turn}] Type a number: "))

for turn in range(1, 10):
    if guess == secret_num:
        print(f"You typed {guess} and got the correct secret number!")
        print("Congratulations!")
        break
    elif guess > secret_num and attempts > 0:
        attempts -= 1
        turn += 1
        print(f"You typed {guess}, but it is an incorrect answer. Try something smaller")
        print(f"You now have {attempts} attempts")
        guess = int(input(f"[Turn nº{turn}] Type a number: "))
    elif guess < secret_num and attempts > 0:
        attempts -= 1
        turn += 1
        print(f"You typed {guess}, but it is an incorrect answer. Try something bigger")
        print(f"You now have {attempts} attempts")
        guess = int(input(f"[Turn nº{turn}] Type a number: "))
    else:
        print("You lost.")
        break
