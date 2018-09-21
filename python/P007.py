from math import ceil
################################################################################
def P007() -> int:
    """
    Find the 10001st prime
    """
    i = 10001
    n = 1

    while i > 1: # offset for starting at 3
        n += 2 # only check odd numbers
        for f in range(2, int(n**0.5)+1): # only check for factors up to sqrt(n)
            if n % f == 0:
                i += 1
                break
        i -= 1

    return n

if __name__=="__main__":
    print(P007())
