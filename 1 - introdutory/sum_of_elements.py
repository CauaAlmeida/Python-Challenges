counter = int(input("Type how many numbers you want to add to the list:"))

lst = []

for i in range(1, counter + 1):
    num = int(input("Type a number: "))
    lst.append(num)

soma = sum(lst)

print(soma)
