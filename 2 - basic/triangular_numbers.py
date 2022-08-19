""" GOAL: finding the nth triangular number """
""" n(n+1)/2 """

n = int (input("Type the nth triangular number you want to find: "))

def triangularNumber( n ):
    if n == 0:
        print("Zero is not a valid option. Try again.")
        n = int (input("Type the nth triangular number you want to find: "))
        triangularNumber( n )
    elif n < 0:
        print("Negative numbers are not a valid input. Try again")
        n = int (input("Type the nth triangular number you want to find: "))
        triangularNumber( n )
    else:
        return int(n * ( n + 1 ) / 2)
    
print([triangularNumber(n) for n in range(n)])