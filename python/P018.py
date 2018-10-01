from typing import Dict,Tuple,List
################################################################################
def P018() -> int:
    """
    Find the max sum from top to bottom (only moving adjacent spaces)
    """
    data = """
                             75
                           95 64
                          17 47 82
                         18 35 87 10
                       20 04 82 47 65
                     19 01 23 75 03 34
                    88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
              41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    # Parse data
    lines = data.strip().split('\n')
    nums = [list(map(int,row.strip().split())) for row in lines]
    # Recursive solution
    return best(14,0,nums,{})

def best(row : int, col : int, data : List[List[int]],
         cache : Dict[Tuple[int,int],int]
         ) -> int:
    """ The value of the best path from a given point in the grid """
    if (row,col) in cache:
        return cache[(row,col)]
    else:
        currval = data[-row-1][col]
        if row == 0:
            val = currval
        else:
            kwargs = {'row':row-1,'data':data,'cache':cache}
            val = currval + max(best(col=col,**kwargs),best(col=col+1,**kwargs)) # type: ignore
        cache[(row,col)] = val
        return val



if __name__=="__main__":
    print(P018())