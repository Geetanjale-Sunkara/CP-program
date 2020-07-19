# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
# which is the value of the middle element, or the average of the two middle elements if there is no single middle
# element. If the list is empty, return None.


def median(a):
    # your code goes here
    l = len(a)
    if (l == 0):
        return None
    elif (l == 1):
        return a[0]
    elif (l % 2 != 0):
        return a[int((l-1)/2)]
    else:
        return ((a[int((l/2)-1)]+a[int(l/2)])/2)
