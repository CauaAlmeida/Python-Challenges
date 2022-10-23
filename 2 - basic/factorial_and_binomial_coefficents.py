#   From Conceptual Programming with Python
#   ---------------------------------------
#   Goal: writing a Python function that solves a given factorial of n
#   or a given binomial coefficient of numerator and denominator.
#
#   Factorial: n! = n * ( n - 1 ) * ( n - 2 ) * ... * 1
#   Binomial Coefficient: (numerator/denominator) = numerator! / (numerator-denominator)! * denominator!

print("What do you want to do?\nCalculate factorial = f\nCalculate binomial coefficient = b")

choice = str(input(">> "))

if choice == 'f':
    n = int(input("Type the number you want to apply the factorial formula: "))


    def factorial(x):
        if x == 0:  # Base case
            return 1
        else:
            return x * factorial(x - 1)


    print(f"The factorial of {n} is: {factorial(n)}")
elif choice == 'b':
    numerator = int(input("Numerator: "))
    denominator = int(input("Denominator: "))


    def binomial(a, b):
        if b == 0:  # Base case
            return 1
        elif a == 0:  # Base case
            return 0
        else:
            return factorial(a) // (factorial(a - b) * factorial(
                b))  # // does not return a floating-point value.


    print(binomial(numerator, denominator))
else:
    print("Wrong input!")
