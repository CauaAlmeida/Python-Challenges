x = int(input("How much money did you borrowed? "))
t = float(input("And for how long (in years)? "))
ir = float(input("And at which interest rate(%)? "))

ci = x * (1 + ir / 100) ** t

print(ci)
