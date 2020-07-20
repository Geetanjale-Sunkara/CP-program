# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def fun_hasnoprimes(l):
    for i in l:
        for j in i:
            if (isprime(j)):
                return False
    return True
