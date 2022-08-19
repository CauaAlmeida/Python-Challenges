import random

options = {
    1:"rock",
    2:"paper", 
    3:"scisors",
    }

x = random.randint(1,3)

def main():
    y = input ('Type "rock", "paper" or "scisors": ')
    z = options[x]
    if y == z:
        return "It's a Tie!"
    elif y == "rock":
        if z == "paper":
            return "AI has chosen paper. You lose!"
        else:
            return "AI has chosen scisors. You win!"
    elif y == "paper":
        if z == "scisors":
            return "AI has chosen scisors. You lose!"
        else:
            return "AI has chosen rock. You win!"
    elif y == "scisors":
        if z == "rock":
            return "AI has chosen rock. You lose!"
        else:
            return "AI has chosen paper. You win!"
    else:
        return "Invalid input!"

        
if __name__ == "__main__":
    game = main()
    print(game)
