from typing import Dict,Tuple
################################################################################
def P015() -> int:
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """
    return numroutes(20,20,{})

def numroutes(i:int,j:int,routedict:Dict[Tuple[int,int],int])->int:
    if (i,j) in routedict: # lucky case
        return routedict[(i,j)]
    elif (i==0 or j==0): # edge case
        routedict[(i,j)]=1
        return 1
    else:
        val = numroutes(i,j-1,routedict) + numroutes(i-1,j,routedict)
        routedict[(i,j)] = val
        return val

if __name__=="__main__":
    print(P015())
