# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


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


def fun_nth_happy_number(n):
    num = -1
    i = 1
    while (num < n):
        if (ishappynumber(i)):
            num += 1
        i += 1
    return i-1
