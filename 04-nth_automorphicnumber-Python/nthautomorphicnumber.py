# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.


def isautomorphic(n):
    if (n**2 % (10**(len(str(n)))) == n):
        return True
    return False


def nthautomorphicnumbers(n):
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    l = [0, 1, 5, 6]
    num1 = 5
    l1 = 1
    num2 = 6
    l2 = 1
    cnt = 4
    while (cnt < n):
        for i in range(1, 10):
            nn = i*(10**(l1))+num1
            if (isautomorphic(nn)):
                num1 = nn
                cnt += 1
                break
        for i in range(1, 10):
            nn = i*(10**(l2))+num2
            if (isautomorphic(nn)):
                num2 = nn
                cnt += 1
                break
        if (num1 > num2):
            if num2 not in l:
                l.append(num2)
            if num1 not in l:
                l.append(num1)
        else:
            if num1 not in l:
                l.append(num1)
            if num2 not in l:
                l.append(num2)
        l1 += 1
        l2 += 1
    if len(l) == n:
        return l[len(l)-1]
    else:
        return l[len(l)-2]
