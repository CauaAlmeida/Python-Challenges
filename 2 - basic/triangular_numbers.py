""" GOAL: finding the nth triangular number """
""" x(x+1)/2 """

n = int(input("Type the nth triangular number you want to find: "))


def triangularNumber(x):
    if x == 0:
        print("Zero is not a valid option. Try again.")
        x = int(input("Type the nth triangular number you want to find: "))
        triangularNumber(x)
    elif x < 0:
        print("Negative numbers are not a valid input. Try again")
        x = int(input("Type the nth triangular number you want to find: "))
        triangularNumber(x)
    else:
        return int(x * (x + 1) / 2)


print([triangularNumber(n) for n in range(n)])
