# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def isprime(num):
    if (num == 4):
        return False
    for i in range(2, num//2):
        if (num % i == 0):
            return False
    return True


def isSmith(num):
    nn = num
    nl = list(map(int, list(str(num))))
    l = []
    ll = []
    for i in range(2, (num//2)+1):
        while (num % i == 0):
            ll.append(i)
            n = list(map(int, list(str(i))))
            l.append(sum(n))
            num = num//i
        if (num == 1):
            break
    if (nn == sum(l) or sum(nl) == sum(l)):
        return True
    else:
        return False


def fun_nth_smithnumber(n):
    i = 4
    cnt = -1
    while (cnt < n):
        if isSmith(i):
            cnt += 1
        i += 1
    return i-1
