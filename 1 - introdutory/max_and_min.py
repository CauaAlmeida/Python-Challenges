counter = int (input("Type how many numbers you want to add to the list:" ))

listTest = []

for i in range(1, counter+1):
    num = int (input("Type a number: "))
    listTest.append(num)

largest = max(listTest)
lowest = min(listTest)
print(largest)
print(lowest)
