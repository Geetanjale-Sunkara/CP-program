# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function
# takes two rectangles described this way, and returns True if the rectangles
# overlap at all (even if just at a point), and False otherwise.
# Note: here we will represent coordinates the way they are usually represented in
# computer graphics, where (0,0) is at the left-top corner of the screen, and while
# the x-coordinate goes up while you head right, the y-coordinate goes up while you
# head down (so we say that "up is down")


def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    l1 = left1
    r1 = top1
    l2 = l1+width1
    r2 = r1+height1
    l3 = left2
    r3 = top2
    l4 = l2+width2
    r4 = r2+height2
    if((l2 >= l3 and l1 <= l4) or (r1 >= r4 and r2 <= r3)):
        return True
    else:
        return False
