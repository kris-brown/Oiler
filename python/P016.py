import numpy as np # type: ignore
################################################################################
def P016() -> int:
    """
    What is the sum of the digits of the number 2^1000?
    """
    digs = np.array([0,1]) # start with 2 ** 0
    for pow in range(1000):
        digs *= 2
        if digs[0] != 0:
            digs = np.concatenate(([0],digs))
        for i in reversed(range(0,len(digs))):
            dig = digs[i]
            if dig > 9:
                digs[i]      = dig % 10
                digs[i - 1] += 1 # never have to carry over anything else

    return sum(digs)


if __name__=="__main__":
    print(P016())
