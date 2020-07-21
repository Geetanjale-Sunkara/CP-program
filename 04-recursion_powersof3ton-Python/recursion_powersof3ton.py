# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.
import math


def recursion_powersof3ton(n):
    if math.floor(n) == 1 or math.floor(n) == 2:
        return [1]
    elif math.floor(n) <= 0:
        return None
    l = recursion_powersof3ton(n/3)
    l.append(l[len(l)-1]*3)
    return l
