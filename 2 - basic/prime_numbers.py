def isprime (num):
    for i in range (2,num):
        if (num % i) == 0:
            return False
    return True

if __name__ == "__main__":
    num = int (input ("Type a number to check if it is a prime number: "))
    x = isprime(num)
    if x:
        print (f'{num} is a prime number')
    else:
        print (f'{num} is not a prime number')