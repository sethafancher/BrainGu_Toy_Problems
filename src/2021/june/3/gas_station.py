# Have the function GasStation(strArr) take strArr which will be an an array consisting of the following elements: 
# N which will be the number of gas stations in a circular route and each subsequent element will be the 
# string g:c where g is the amount of gas in gallons at that gas station and c will be the amount of gallons of gas 
# needed to get to the following gas station.
# For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. 
# Your goal is to return the index of the starting gas station that will allow you to travel around the whole route 
# once, otherwise return the string impossible. 
# For the example above, there are 4 gas stations, and your program should return the string 1 because starting at 
# station 1 you receive 3 gallons of gas and spend 1 getting to the next station. 
# Then you have 2 gallons + 2 more at the next station and you spend 2 so you have 2 gallons when you get to the 
# 3rd station. You then have 3 but you spend 2 getting to the final station, 
# and at the final station you receive 0 gallons and you spend your final gallon getting to your starting point. 
# Starting at any other gas station would make getting around the route impossible, so the answer is 1. 
# If there are multiple gas stations that are possible to start at, return the smallest index (of the gas station). 
# N will be >= 2.

def gas_station(str):
  # parsing the string array
  gas = []
  cost = []
  numStations = int(str[0])
  i = 1
  while i <= numStations:
    gasCurr = ""
    costCurr = ""
    j = 0
    while str[i][j] != ":":
      gasCurr += str[i][j]
      j += 1
    j += 1
    while j < len(str[i]):
      costCurr += str[i][j]
      j += 1
    gas.append(int(gasCurr))
    cost.append(int(costCurr))
    i += 1
  # algorithm
  if sum(gas) < sum(cost):
    return "impossible"
  tank = 0
  begin = 0
  for i in range(numStations):
    tank += (gas[i] - cost[i])
    if tank < 0:
      tank = 0
      begin = i + 1
  return begin + 1