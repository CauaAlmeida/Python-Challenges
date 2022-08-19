import math

n1 = int (input("Type a number: "))
n2 = int (input("Type a number: "))

def higherNum( n1, n2 ):
    if n1 > n2:
        return(f"Out of the numbers you've typed, the larger one is {n1}.")
    elif n1 == n2:
        return(f"Out of the numbers you've typed, both numbers are equal.")
    else:
        return(f"Out of the number you've typed, the larger one is {n2}.")
        
print(higherNum( n1, n2 ))

## NOW LET'S NOT OVER COMPLICATE IT

largest = max(n1, n2)
print("Largest number you entered is: ", largest)