# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    i = s1.find(s2)
    j = 0
    if (i == -1):
        return s1
    out = ""
    while i != -1:
        out += s1[j:i]
        out += s3
        j = i+len(s2)
        i = s1.find(s2, i+1, len(s1))
    out += s1[j:]
    return out
