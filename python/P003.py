def P003()->int:
    """Determine largest prime factor of 600851475143"""
    n = 600851475143 # input
    factor = 1       # container for result

    # Iteratively peel off prime factors until we've factorized n
    while n > 1:
        found = False
        for i in range(2, int(n ** 0.5)): # if we don't find something before sqrt(n), then n is prime
            if n % i == 0: # n is composite
                factor = max(i, factor)
                n = n // i # try again with reduced input
                found = True
                break
        if not found: # n is prime - we're done factorizing!
            factor = max(factor, n)
            break
    return factor

if __name__=="__main__":
    print(P003())
