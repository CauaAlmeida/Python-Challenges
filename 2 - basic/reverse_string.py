def reverse(str):
    reversed = ""
    for char in str:
        reversed = char + reversed
    return reversed


str = input("Input what you want to reverse: ")
n = reverse(str)
print(n)
