# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46


def istidy(n):
    l = list(map(int, list(str(n))))
    if (l == sorted(l)):
        return True
    return False


def fun_nth_tidynumber(n):
    i = 1
    cnt = 0
    while (cnt < n):
        i += 1
        if (i < 9):
            cnt += 1
        elif(istidy(i)):
            cnt += 1
    return i
