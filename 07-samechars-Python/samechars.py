# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either
# parameter is not a string, but returns True if both strings are empty (why?).


def samechars(s1, s2):
    ss1 = list(dict.fromkeys(list(str(s1))))
    ss2 = list(dict.fromkeys(list(str(s2))))
    if (sorted(ss1) == sorted(ss2)):
        return True
    else:
        return False
