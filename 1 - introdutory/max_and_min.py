counter = int (input("Type how many numbers you want to add to the list:" ))

list = []

for i in range(1, counter+1):
    num = int (input("Type a number: "))
    list.append(num)

largest = max(list)
lowest = min(list)
print(largest)
print(lowest)