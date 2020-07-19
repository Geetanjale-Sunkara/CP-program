"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(a, l, h):
    i = l-1
    p = a[h]
    for j in range(l, h):
        if a[j] <= p:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[h] = a[h], a[i+1]
    return i+1


def quicksortt(a, l, h):
    if l < h:
        pi = partition(a, l, h)
        quicksortt(a, l, pi-1)
        quicksortt(a, pi+1, h)
    return a


def quicksort(array):
    # Your code goes here
    return quicksortt(array, 0, len(array)-1)
