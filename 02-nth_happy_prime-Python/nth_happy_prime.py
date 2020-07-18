# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def ishappynumber(n):
    # your code goes here
    if (n == 1):
        return True
    elif(n == 4 or n <= 0):
        return False
    else:
        num = n
        sum = 0
        while(num > 0):
            rem = num % 10
            sum = sum+(rem**2)
            num = num//10
        return ishappynumber(sum)


def fun_nth_happy_prime(n):
    num = -2
    i = 1
    while (num < n):
        if (i % 2 != 2):
            if (ishappynumber(i)):
                num += 1
        i += 2
    return i-2
