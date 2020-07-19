# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def fun_nth_palindromic_prime(n):
    cnt = -1
    ii = 2
    while (cnt < n):
        nn = str(ii)
        if (nn == nn[::-1] and isprime(ii)):
            cnt += 1
    return ii-1
