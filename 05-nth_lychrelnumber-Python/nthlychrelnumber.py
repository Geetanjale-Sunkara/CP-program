# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def isplychrel(n):
    i = 0
    f = False
    while n != int((str(n))[::-1]):
        n = n+int((str(n))[::-1])
        i += 1
        if i == 30:
            f = True
            break
    return f


def nthlychrelnumbers(n):
    i = 196
    cnt = 1
    while (cnt < n):
        i += 1
        if (isplychrel(i)):
            cnt += 1
    return i
