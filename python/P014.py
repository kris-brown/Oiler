from typing import Dict
################################################################################
def P014() -> int:
    """
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Terminate at n = 1
    Which starting number < 1e6 produces the longest chain?
    """
    cdict = {1:1}
    maxlen = 1
    maxnum = 1

    def collatz(i:int,d:Dict[int,int])->int:
        if i in d:
            return d[i]
        elif i % 2:
            return 1 + collatz(3*i+1,d)
        else:
            return 1 + collatz(i//2,d)

    for i in range(2,1000000):
        length = collatz(i,cdict)
        cdict[i]= length
        if length > maxlen:
            maxnum = i
            maxlen = length

    return maxnum


if __name__=="__main__":
    print(P014())
