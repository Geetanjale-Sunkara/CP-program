# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isprime(self, num):
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def fun_nth_additive_prime(n):
    cnt = 0
    i = 2
    while (cnt < n):
        nn = str(n)
        l = list(map(int, list(nn)))
        sum = 0
        for i in l:
            sum += i
        if (self.isprime(i)):
            cnt += 1
        i += 1
    return i-1
