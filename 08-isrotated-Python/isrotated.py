# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    if (str1[::-1] == str2):
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
