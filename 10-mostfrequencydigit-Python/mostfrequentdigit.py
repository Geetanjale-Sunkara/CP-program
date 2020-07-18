# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.


def mostfrequentdigit(n):
    # your code goes here
    nn = str(n)
    l = list(map(int, list(nn)))
    num = l[0]
    for i in l:
        if (l.count(num) <= l.count(i)):
            num = i
    return num
