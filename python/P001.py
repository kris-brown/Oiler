def P001()->int:
    """Finds the sum of all multiples of 3 or 5 below 1000. """
    tot = 0
    for i in range(1000):
      if (i % 3 == 0 or i % 5 == 0):
        tot += i;
    return tot

if __name__=='__main__':
    P001()
