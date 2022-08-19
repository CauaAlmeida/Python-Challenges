import math

# perimeter = sum of each side of the triangle

a = float (input("What is the the length of the side a of the triangle? "))
b = float (input("What is the the length of the side b of the triangle? "))
c = float (input("What is the the length of the side c of the triangle? "))

p = (a + b + c) / 2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))

print (area)