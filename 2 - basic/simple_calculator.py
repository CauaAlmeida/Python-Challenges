def soma(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def mul(x, y):
    print(x * y)


def div(x, y):
    print(x / y)


def operation():
    z = arithmetics[op]
    z(n1, n2)


arithmetics = {
    1: soma,
    2: sub,
    3: mul,
    4: div,
}

n1 = int(input("Type the first number you want to use in the operation: "))
n2 = int(input("Type the second number you want to use in the operation: "))
op = int(input(
    "Chose the arithmetical operation you want to do with such numbers [sum = 1 | sub = 2 | mul = 3 | div = 4]: "))
operation()
