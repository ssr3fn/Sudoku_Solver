from math import *
class SudokuSolver:
    def __init__(self,dim):
        self.dim=dim
        self.grid= [[" " for i in range(dim)] for j in range(dim)]
    def printGrid(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.grid[i][j],end = " ")
            print("\n",end="") 
    def check(self,c,i,j):
        a=int(sqrt(self.dim))
        for n in range(self.dim):
            if i!=n and self.grid[n][j]==c:
                return False
            if j!=n and self.grid[i][n]==c:
                return False
        for k in range((i//a)*(a),(i//a)*(a)+a):
            for l in range((j//a)*(a),(j//a)*(a)+a):
                if i==k and j==l:
                    continue
                if self.grid[k][l]==c:
                    return False
        return True
    def solve(self):
        a=False
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grid[i][j]!='.':
                    continue
                for c in range(self.dim):
                    if(self.check(str(c+1),i,j)):
                        self.grid[i][j]=str(c+1)
                        a=self.solve()
                        if a:
                            return True
                        self.grid[i][j]='.'
                if self.grid[i][j]=='.':
                    return False
        return True
    def input(self,i):
        row=input()
        for j in range(self.dim):
            self.grid[i][j]=row[j]