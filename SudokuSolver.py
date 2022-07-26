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
    def checkGrid(self):
        a=[]
        b=[]
        c=int(sqrt(self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grid[i][j]!='.' and self.grid[i][j] in a:
                    return False
                a.append(self.grid[i][j])
                if self.grid[j][i]!='.' and self.grid[j][i] in b:
                    return False
                b.append(self.grid[j][i])
            a.clear()
            b.clear()
        for i in range(self.dim):
            for j in range((i//c)*c,(i//c)*c+c):
                for k in range((i%c)*c,(i%c)*c+c):
                    if self.grid[j][k]=='.':
                        continue
                    if self.grid[j][k] in a:
                        return False
                    a.append(self.grid[j][k])
            a.clear()
        return True 
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
