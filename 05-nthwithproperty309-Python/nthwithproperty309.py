# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.


def is309(n):
    l = list(map(int, list(str(n**5))))
    if l.count(0) == 0:
        return False
    if l.count(1) == 0:
        return False
        if l.count(2) == 0:
            return False
        if l.count(3) == 0:
            return False
        if l.count(4) == 0:
            return False
        if l.count(5) == 0:
            return False
        if l.count(6) == 0:
            return False
        if l.count(7) == 0:
            return False
        if l.count(8) == 0:
            return False
        if l.count(9) == 0:
            return False
        return True


def nthwithproperty309(n):
    # Your code goes here
    i = 309
    cnt = -1
    while (cnt < n):
        if (is309(i)):
            cnt += 1
        i += 1
    return i-1
