# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L
# contains any duplicate values (that is,
# if any two values in L are equal to each other), and False otherwise.


def hasduplicates(L):
    # Your code goes here
    for i in L:
        for j in i:
            if (sum(x.count(j) for x in L) > 1):
                return True
    return False
