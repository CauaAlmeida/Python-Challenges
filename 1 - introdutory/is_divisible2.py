num = int(input('Input a number to see if it is divisible by 3 and 5: '))
r1 = num % 3
r2 = num % 5

if r1 == 0 and r2 == 0:
    print(f"{num} is divisible by three and five.")
elif r1 == 0:
    print(f"{num} is divisible by three, but not by five.")
elif r2 == 0:
    print(f"{num} is divisible by five, but not by five.")
else:
    print(f"{num} is neither divisible by divisible by three or five.")