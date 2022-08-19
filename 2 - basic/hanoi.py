#   From Conceptual Programming with Python
#   ---------------------------------------
#   Goal: writing a Python function that solves the problem for any number of disks. 
#

""" 

n = number of disks;
f = from;
h = helper rod;
t = to; 

"""

n = int(input("What is the number of disks: "))

def hanoi_game(n,rodFrom,rodHelper,rodTo):
    if n == 0:
        pass
    else:
        hanoi_game(n-1,rodFrom,rodTo,rodHelper)
        print(f"Move object from {rodFrom} to {rodTo}!")
        hanoi_game(n-1,rodHelper,rodFrom,rodTo)

print(hanoi_game(n,"A","B","C"))