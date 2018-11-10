import itertools
import time
import math
n=23

def printmatrix():
    nq = marked()
    nqueens(nq,0)

def marked():
    nq = [0]*n
    for rc in range(n):
        nq[rc] = [0]*n
    return nq

def feasible(nq, r, c):
    for i in range(c):
        if nq[r][i] == 1:
            return False
 
    for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
        if nq[i][j] == 1:
            return False
 
    for i,j in zip(range(r,n,1), range(c,-1,-1)):
        if nq[i][j] == 1:
            return False
    return True

def nqueens(nq, c):
    if c >= n:
        return True
    
    for i in range(n):
        if feasible(nq, i, c):
            nq[i][c] = 1
            if c == n-1 :
                for x in range(n):
                    for y in range(n):
                        if nq[x][y] == 1:
                            print('[',x,',',y,']',end='\t')
                print()
                nq[i][c] = 0
                return 
            nqueens(nq, c+1)     
            nq[i][c] = 0

printmatrix()
