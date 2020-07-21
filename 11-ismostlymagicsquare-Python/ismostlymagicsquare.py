# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.


def ismostlymagicsquare(a):
    # Your code goes here
    sd = 0
    sd2 = 0
    j = len(a)-1
    for i in range(len(a)):
        sd += a[i][i]
        sd2 += a[i][j]
        j -= 1
    if (sd == sd2):
        sr = 0
        sc = 0
        for i in range(len(a)):
            for j in range(len(a)):
                sr += a[i][j]
                if (j == len(a)-1):
                    if (sr != sd):
                        return False
                    sr = 0
                sc += a[j][i]
                if (j == len(a)-1):
                    if (sc != sd):
                        return False
                    sc = 0
    else:
        return False
    return True
