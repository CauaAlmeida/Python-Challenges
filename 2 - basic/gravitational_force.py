""" GRAVITATIONAL FORCE ( F = G m^1m^2/r^2 ) """

g = 6.673 * (10 ** -11)

m1 = float(input("What is the mass of the first object in kg? "))
m2 = float(input("What is the mass of the second object in kg? "))
r = float(input("What is the distance between them in meters? "))

force = (g * m1 * m2) / (r ** 2)

print(f"The gravitational force is {force} N")
