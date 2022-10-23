x = int(input("How much money did you borrowed? "))
t = float(input("And for how long (in years)? "))
ir = float(input("And at which interest rate(%)? "))

sr = x * t * (ir/100)

print(sr)
