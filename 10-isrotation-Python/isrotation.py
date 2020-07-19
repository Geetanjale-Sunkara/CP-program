# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.


def isrotated(str1, str2):
    # Your code goes here
    if (str1[::-1] == str2 or str1 == str2):
        return True
    x = str1[1:]+str1[0]
    while x != str1:
        if (x == str2):
            return True
        x = x[1:]+x[0]
    x = str1[len(str1)-1]+str1[:len(str1)-1]
    while x != str1:
        if (x == str2):
            return True
        x = x[len(x)-1]+x[:len(x)-1]
    return False


def isrotation(x, y):
    # Your code goes here
    xx = str(x)
    yy = str(y)
    return isrotated(xx, yy)
