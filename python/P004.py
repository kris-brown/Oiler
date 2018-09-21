def P004() -> int:
    """A palindromic number reads the same both ways.
        The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
        Find the largest palindrome made from the product of two 3-digit numbers."""
    best= 0
    for i in range(100,1000):
        for j in range(i,1000):
            ij = i * j
            if pallindrome(ij):
                best = max(ij,best)
    return best

def pallindrome(i:int)->bool:
    stri = str(i)
    half = str(i)[:len(stri)//2]
    for ind,val in enumerate(half):
        if stri[-ind-1] != val:
            return False
    return True

if __name__=="__main__":
    print(P004())
