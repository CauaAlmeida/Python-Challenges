n1 = int(input("Type a number: "))
n2 = int(input("Type a number: "))


def higherNum(x, y):
    if x > y:
        return f"Out of the numbers you've typed, the larger one is {x}."
    elif x == y:
        return f"Out of the numbers you've typed, both numbers are equal."
    else:
        return f"Out of the number you've typed, the larger one is {y}."


print(higherNum(n1, n2))

# NOW LET'S NOT OVERCOMPLICATE IT

largest = max(n1, n2)
print("Largest number you entered is: ", largest)
