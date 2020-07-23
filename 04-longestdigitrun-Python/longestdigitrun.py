# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).


def longestdigitrun(n):
    n = abs(n)
    l = list(map(int, list(str(n))))
    cnt = 0
    mcnt = 0
    num = n
    for i in range(1, len(l)):
        if (l[i-1] == l[i]):
            cnt += 1
        else:
            if (mcnt < cnt):
                num = l[i-1]
            elif (mcnt == cnt and num < l[i-1]):
                num = l[i-1]
    return num
