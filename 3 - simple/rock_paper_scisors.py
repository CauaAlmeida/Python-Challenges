import random

options = {
    1: "rock",
    2: "paper",
    3: "scissors",
}

x = random.randint(1, 3)


def main():
    y = input('Type "rock", "paper" or "scissors": ')
    z = options[x]
    if y == z:
        return "It's a Tie!"
    elif y == "rock":
        if z == "paper":
            return "AI has chosen paper. You lose!"
        else:
            return "AI has chosen scissors. You win!"
    elif y == "paper":
        if z == "scissors":
            return "AI has chosen scisosrs. You lose!"
        else:
            return "AI has chosen rock. You win!"
    elif y == "scissors":
        if z == "rock":
            return "AI has chosen rock. You lose!"
        else:
            return "AI has chosen paper. You win!"
    else:
        return "Invalid input!"


if __name__ == "__main__":
    game = main()
    print(game)
