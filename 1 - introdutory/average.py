counter = int(input("How many numbers you want to enter: "))

nums = []

for i in range(1, counter+1):
    inputs = int(input(f"You've decided to enter {counter} numbers. Enter number {i}: "))
    nums.append(inputs)


total = sum(nums)

average = total / counter

print(round(average))
