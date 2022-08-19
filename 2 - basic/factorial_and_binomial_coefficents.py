#   From Conceptual Programming with Python
#   ---------------------------------------
#   Goal: writing a Python function that solves a given factorial of n
#   or a given binomial coefficent of numerator and denominator.
#
#   Factorial: n! = n * ( n - 1 ) * ( n - 2 ) * ... * 1
#   Binomial Coefficent: (numerator/denominator) = numerator! / (numerator-denominator)! * denominator!

print("What do you want to do?\nCalculate factorial = f\nCalculate binomial coefficent = b")

choice = str (input(">> "))
def factorial(n):
        if n == 0: # Base case
            return 1
        else:
            return n * factorial(n-1)

if choice == 'f':
    n = int(input("Type the number you want to aply the factorial formula: "))
    def factorial(n):
            if n == 0: # Base case
                return 1
            else:
                return n * factorial(n-1)
    print(f"The factorial of {n} is: {factorial(n)}")
elif choice == 'b':
    numerator = int (input("Numerator: "))
    denominator = int (input("Denominator: "))
    def binom(numerator,denominator) :
        if denominator == 0 : # Base case
            return 1
        elif numerator == 0 : # Base case
            return 0
        else :
            return factorial(numerator) // (factorial(numerator - denominator) * factorial(denominator)) # // does not return a floating-point value.
    print(binom(numerator,denominator))
else:
    print("Wrong input!")