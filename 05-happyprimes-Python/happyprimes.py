# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!


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


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def ishappyprimenumber(n):
    # Your code goes here
    if (isprime(n)):
        if(ishappynumber(n)):
            return True
    return False
