import math
# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.


def trianglearea(s1, s2, s3):
    # your code goes here
    if(s1+s2 > s3 and s2+s3 > s1 and s3+s1 > s2):
        return (0.25)*((s1+s2+s3)*(s1+s2-s3)*(s1+s3-s2)*(s3+s2-s1))**0.5
    else:
        return 0


def fun_distance(x1, y1, x2, y2):
    return (math.sqrt((x2-x1)**2+(y2-y1)**2))


def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    # your code goes here
    return trianglearea(fun_distance(x1, y1, x2, y2), fun_distance(x2, y2, x3, y3), fun_distance(x1, y1, x3, y3))
