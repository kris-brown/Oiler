from typing import List
from math import gcd
from functools import reduce
################################################################################
def P005() -> int:
    """2520 is the smallest number that can be divided by each of the numbers
        from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the
     numbers from 1 to 20?"""
    factors = [2520,19,18,17,16,15,14,13,12,11] # others are irrelevant as they divide other factors
    return lcms(factors)

def lcm(a : int, b : int) -> int:
    return a * b // gcd(a, b)

def lcms(numbers : List[int]) -> int:
     return reduce(lcm, numbers)


if __name__=="__main__":
    print(P005())
