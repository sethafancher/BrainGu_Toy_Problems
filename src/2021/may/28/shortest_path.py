# Have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph.
# The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. 
# The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the 
# array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). 
# Although, there may exist no connections at all.
# An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last 
# Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being 
# ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G.
# There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. 
# Also, the connection A-B for example, means that A can get to B and B can get to A.
from collections import defaultdict

def pathCreater(newPath):
  sol = ""
  for i in range(len(newPath)):
    sol += (newPath[i] + "-")
  sol = sol[:-1]
  print(sol)
  return sol

def shortest_path(str):
  numNodes = int(str[0])
  connections = defaultdict(list)
  i = 1
  while i < (numNodes + 1):
    i += 1
  nodeEnd = i - 1
  nodeLength = len(str[nodeEnd])
  while i < len(str):
    connections[str[i][:nodeLength]].append(str[i][nodeLength+1:])
    connections[str[i][nodeLength+1:]].append(str[i][:nodeLength])
    i += 1
  explored = []
  queue = [[str[1]]]
  while queue:
    currPath = queue.pop(0)
    node = currPath[-1]
    if node not in explored:
      neighbors = connections[node]
      for neighbor in neighbors:
        newPath = list(currPath)
        newPath.append(neighbor)
        queue.append(newPath)
        if neighbor == str[nodeEnd]:
          return pathCreater(newPath)
      explored.append(node)
  return -1
