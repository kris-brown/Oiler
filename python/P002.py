def P002()->int:
    """ Finds the sum of the even-valued Fibonacci terms < 4e6 """
    # Initialize variables
    penultimate = 1
    ultimate    = 1
    current     = 2
    tot         = 0
    
    # Main loop
    while current < 4e6:
        if current % 2 == 0 :
            tot +=  current
        antepenultimate = penultimate
        penultimate     = ultimate
        ultimate        = current
        current         = antepenultimate + penultimate

    return tot
if __name__=='__main__':
    P002()
