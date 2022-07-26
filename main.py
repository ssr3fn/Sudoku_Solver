from SudokuSolver import SudokuSolver
#Dimension of the grid is the number of rows or columns in the grid
#It should be a perfect square
#Normal Sudoku grid has a dimension of 9
n=int(input("Enter dimension of Sudoku Grid: "))
sudoku=SudokuSolver(n)
print("Enter Grid: ")
#Enter each row in a separate line and write the numbers without any spaces
#For unfilled boxes put a '.' instead of the number
for i in range(n):
    sudoku.input(i)
a=sudoku.solve()
if not a:
    print("No solution exists.")
else:
    sudoku.printGrid()