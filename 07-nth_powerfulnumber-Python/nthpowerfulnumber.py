# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def ispowerfulnum(n):
    ll = []
    for i in range(2, (n//2)+1):
        if (n % i == 0 and isprime(i)):
            ll.append(i)
    if (ll == []):
        return False
    for i in ll:
        if n % (i**2) != 0:
            return False
    return True


def nthpowerfulnumber(n):
    i = 1
    cnt = 0
    while (cnt < n):
        i += 1
        if (ispowerfulnum(i)):
            cnt += 1
    return i
