# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, int(num**(1/2))+1):
        if (num % i == 0):
            return False
    return True


def isugly(n):
    if n <= 5:
        return True
    if (isprime(n)):
        return False
    l = [2, 3, 5]
    for i in range(2, n//2):
        if isprime(i):
            if (n % i == 0 and (i not in l)):
                return False
    return True


def fun_nth_uglynumber(n):
    i = 1
    cnt = 0
    while (cnt < n):
        i += 1
        if (isugly(i)):
            cnt += 1
    return i
