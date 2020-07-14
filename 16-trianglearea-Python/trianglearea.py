# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):
    # your code goes here
    if(s1+s2 > s3 and s2+s3 > s1 and s3+s1 > s2):
        return (0.25)*((s1+s2+s3)*(s1+s2-s3)*(s1+s3-s2)*(s3+s2-s1))**0.5
    else:
        return 0
