# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def iscircularprime(n):
    if isprime(n):
        num = (n % 10)*10**(len(str(n))-1)+n // (10**(len(str(n))-1))
        while (num != n):
            if (isprime(num) == False):
                return False
            num = (num % 10)*10**(len(str(num))-1)+num//(10**(len(str(num))-1))
        return True
    return False


def nthcircularprime(n):
    i = 2
    cnt = 0
    while (cnt < n):
        i += 1
        if (iscircularprime(i)):
            cnt += 1
    return i
