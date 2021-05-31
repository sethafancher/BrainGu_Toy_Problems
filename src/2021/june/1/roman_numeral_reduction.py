# Have the function RomanNumeralReduction(str) read str which will be a string of roman numerals in decreasing order. 
# The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000.
# Your program should return the same number given by str using a smaller set of roman numerals. 
# For example: if str is "LLLXXXVVVV" this is 200, 
# so your program should return CC because this is the shortest way to write 200 using the roman numeral system given above. 
# If a string is given in its shortest form, just return that same string.
import sys

def roman_numeral_reduction(str):
  total = 0
  sol = ""
  numerals = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]
  for num in str:
    if num == "I":
      total += numerals[0][1]
    elif num == "V":
      total += numerals[1][1]
    elif num == "X":
      total += numerals[2][1]
    elif num == "L":
      total += numerals[3][1]
    elif num == "C":
      total += numerals[4][1]
    elif num == "D":
      total += numerals[5][1]
    else:
      total += numerals[6][1]
  i = len(numerals) - 1
  while total > 0:
    quotient = total // numerals[i][1]
    total = total % numerals[i][1]
    while quotient > 0:
      sol += numerals[i][0]
      quotient -= 1
    i -= 1
  return sol
    
