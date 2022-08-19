def isprime (num):
    for i in range (2,num):
        if (num % i) == 0:
            return False
    return True

def allprimes (num):
    primes = []
    for n in range (2,num+1):
        if isprime(n) is True:
            primes.append(n)
    return primes

if __name__ == "__main__":
    num = int (input ("Type a number to check if it is a prime number: "))
    x = allprimes(num)
    print (x)