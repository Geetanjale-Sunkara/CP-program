# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.
import math


def iskaprekar(num):
    n = num**2
    for i in range(1, len(str(n))):
        m = n % (10**i)
        k = n//(10**i)
        if (m+k == num and k != 0 and m != 0):
            return True
    return False


def fun_nth_kaprekarnumber(n):
    i = 1
    cnt = 0
    while (cnt < n):
        i += 1
        if (iskaprekar(i)):
            cnt += 1
    return i
