#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

counter = int (input("Type how many numbers you want to analyze: "))
def fizzBuzz(n):    
    for i in range (1, counter+1):
        div3 = i % 3
        div5 = i % 5
        if div3 == 0 and div5 == 0:
            print('FizzBuzz')
        elif div3 == 0:
            print('Fizz')
        elif div5 == 0:
            print('Buzz')
        else:
            print(i)
            return
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)