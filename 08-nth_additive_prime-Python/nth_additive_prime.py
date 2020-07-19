# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def fun_nth_additive_prime(n):
    cnt = -1
    ii = 2
    while (cnt < n):
        nn = str(ii)
        l = list(map(int, list(nn)))
        summ = 0
        for i in l:
            summ += i
        if (isprime(ii) and isprime(summ)):
            cnt += 1
        ii += 1
    return ii-1
