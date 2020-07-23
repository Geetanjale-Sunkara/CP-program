# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    l1 = list(map(int, list(str(x))))
    l2 = list(map(int, list(str(y))))
    for i in range(abs(len(l1)-len(l2))):
        if (len(l1) < len(l2)):
            l1.insert(0, 0)
        else:
            l2.insert(0, 0)
    out = [str((l1[i]+l2[i])-10) if l1[i]+l2[i] >=
           10 else str(l1[i]+l2[i]) for i in range(len(l1))]
    return int("".join(out))
