
################################################################################
def P010() -> int:
    """
    Find the sum of all the primes below two million.
    """
    tot = 2
    for n in range(3,2000000,2):
        prime = True
        for f in range(2, int(n**0.5)+1): # only check for factors up to sqrt(n)
            if n % f == 0:
                prime = False
                break
        if prime: tot+=n
    return tot

if __name__=="__main__":
    print(P010())
