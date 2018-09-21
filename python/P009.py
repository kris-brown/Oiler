
################################################################################
def P009() -> int:
    """
    There exists exactly one Pythagorean triplet (a^2+b^2=c^2, a<b<c) for which
    a + b + c = 1000. Find the product abc.

    a+b+sqrt(a^2+b^2)
    """

    for a in range(100,1000):
        for b in range(a+1,1000):
            c2 = a**2+b**2
            c  = (c2)**(0.5)
            if int(c) == c:
                if 1000 == a + b + c:
                    return a*b*int(c)
    raise ValueError()

if __name__=="__main__":
    print(P009())
