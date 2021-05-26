# Have the function SudokuQuadrantChecker(strArr) read the strArr parameter being passed which will represent a 9x9 Sudoku board of integers 
# ranging from 1 to 9. The rules of Sudoku are to place each of the 9 integers integer in every row and column and not have any integers repeat in the respective row, 
# column, or 3x3 sub-grid. The input strArr will represent a Sudoku board and it will be structured in the following format: ["(N,N,N,N,N,x,x,x,x)","(...)","(...)",...)] 
# where N stands for an integer between 1 and 9 and x will stand for an empty cell. Your program will determine if the board is legal; the board also does not necessarily 
# have to be finished. If the board is legal, your program should return the string legal but if it isn't legal, it should return the 3x3 quadrants (separated by commas) 
# where the errors exist. The 3x3 quadrants are numbered from 1 to 9 starting from top-left going to bottom-right.
# For example, if strArr is: ["(1,2,3,4,5,6,7,8,1)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(1,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)"] then your program should return 1,3,4 since the errors are in quadrants 1, 3 and 4 because of the repeating integer 1.
# Another example, if strArr is: ["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,1,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,9)"] then your program should return 3,4,5,9.

def quad(i, j):
    if 0 <= i and i <= 2 and 0 <= j and j <= 2:
      return 1
    elif 0 <= i and i <= 2 and 3 <= j and j <= 5:
      return 2
    elif 0 <= i and i <= 2 and 6 <= j and j <= 8:
      return 3
    elif 3 <= i and i <= 5 and 0 <= j and j <= 2:
      return 4
    elif 3 <= i and i <= 5 and 3 <= j and j <= 5:
      return 5
    elif 3 <= i and i <= 5 and 6 <= j and j <= 8:
      return 6
    elif 6 <= i and i <= 8 and 0 <= j and j <= 2:
      return 7
    elif 6 <= i and i <= 8 and 3 <= j and j <= 5:
      return 8
    else:
      return 9

def sudokuQuadrantChecker(strArray):
  errors = set()
  legal = True
  for i in range(9): # remove all extra characters
    strArray[i] = strArray[i].replace(",", "")
    strArray[i] = strArray[i].replace("(", "")
    strArray[i] = strArray[i].replace(")", "")  
  for i in range(9):
    currRow = {}
    currCol = {}
    currQuad = {}
    row = 3 * (i // 3)
    col = 3 * (i % 3)
    for j in range(9):
      if (strArray[i][j] != "x") and (strArray[i][j] in currRow):
        errors.add(quad(i, j))
        errors.add(currRow[strArray[i][j]])
        legal = False
      currRow[strArray[i][j]] = quad(i, j)
      if (strArray[j][i] != "x") and (strArray[j][i] in currCol):
        errors.add(quad(j, i))
        errors.add(currCol[strArray[j][i]])
        legal = False
      currCol[strArray[j][i]] = quad(j, i)
      r = row + (j // 3)
      c = col + (j % 3)
      if (strArray[r][c] != "x") and (strArray[r][c] in currQuad):
        errors.add(quad(r, c))
        errors.add(currQuad[strArray[r][c]])
        legal = False
      currQuad[strArray[r][c]] = quad(r, c)
  # prepare to print out errors
  errors = sorted(errors)
  errorsString = ""
  for error in errors:
    errorsString += (str(error) + ",")
  errorsString = errorsString[:-1]
  if legal:
    return "legal"
  else:
    return errorsString

""" TESTER
def main():
    strArray = [
        "(1,2,3,4,5,6,7,8,9)",
        "(x,x,x,x,x,x,x,x,x)",
        "(6,x,5,x,3,x,x,4,x)",
        "(2,x,1,1,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,x)",
        "(x,x,x,x,x,x,x,x,9)",
      ]
    print(sudokuQuadrantChecker(strArray))
  
if __name__ == '__main__':
    main()
"""