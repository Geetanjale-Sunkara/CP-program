# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def istruncatableprime(n):
    for i in range(len(str(n)), 0, -1):
        if (isprime(n % (10**i)) == False) or n % (10**i) == 1 or len(str(n % (10**i))) != i:
            return False
    return True


def fun_nth_lefttruncatableprime(n):
    i = 2
    cnt = 0
    while (cnt < n):
        i += 1
        if (istruncatableprime(i)):
            cnt += 1
    return i
