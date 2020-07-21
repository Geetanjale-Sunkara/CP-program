# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.


def fixmostlymagicsquare(L):
    summ = []
    j = len(a)-1
    sd = 0
    sd2 = 0
    for i in range(len(a)):
        sd += a[i][i]
        sd2 += a[i][j]
        j -= 1
    summ.append(sd)
    summ.append(sd2)
    sr = 0
    sc = 0
    l = []
    for i in range(len(a)):
        for j in range(len(a)):
            sr += a[i][j]
            if (j == len(a)-1):
                summ.append(sr)
                if (sr != sd):
                    if (sr == sd2):
                        sd = sd2
                    else:
                        for k in range(len(a)):
                            l.append([i, k])
                sr = 0
            sc += a[j][i]
            if (j == len(a)-1):
                summ.append(sc)
                if (sc != sd):
                    if (sr == sd2):
                        sd = sd2
                    else:
                        for k in range(len(a)):
                            l.append([k, i])
                sc = 0
    l = sorted(l, key=l.count, reverse=True)
    summ = sorted(summ, key=summ.count, reverse=True)
    n = summ.count(summ[0])
    a[l[0][0]][l[0][1]] = a[l[0][0]][l[0][1]]-abs(summ[0]-summ[n])
    return a
