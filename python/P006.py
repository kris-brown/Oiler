from typing import List
from math import gcd
from functools import reduce
################################################################################
def P006() -> int:
    """
    Find the difference between the sum of the squares of the first one hundred
        natural numbers and the square of the sum.
    """
    
    return sum(range(101))**2 - sum([x**2 for x in range(101)])

if __name__=="__main__":
    print(P006())
