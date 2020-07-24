# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, int(num**(1/2))+1):
        if (num % i == 0):
            return False
    return True


def iscircularprime(n):
    if isprime(n):
        if (n < 9):
            return True
        l = []
        num = (n % 10)*10**(len(str(n))-1)+n // (10)
        while (num != n):
            if len(str(num)) == len(str(n)):
                l.append(num)
            else:
                break
            num = (num % 10)*10**(len(str(num))-1)+num // (10)
        if (l == [] or len(l) != len(str(n))-1):
            return False
        for i in l:
            if (isprime(i) == False):
                return False
        return True
    return False


def nthcircularprime(n):
    i = 2
    cnt = 1
    while (cnt < n):
        i += 1
        if (iscircularprime(i)):
            cnt += 1
    return i
