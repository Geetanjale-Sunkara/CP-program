# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"


def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    m = len(s1)
    n = len(s2)
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    l = 0
    lcs = []
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                cc = c[i][j]+1
                c[i+1][j+1] = cc
                if cc > l:
                    lcs = []
                    l = cc
                    lcs.append(s1[i-c+1:i+1])
                elif cc == l:
                    lcs.append(s1[i-c+1:i+1])
    return lcs[len(lcs)-1]
