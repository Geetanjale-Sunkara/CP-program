import math
# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.


def isperfectsquare(n):
    # your code goes here
    try:
        n = int(n)
        i = int(math.sqrt(n))
        return (n == i**2)
    except:
        return False
