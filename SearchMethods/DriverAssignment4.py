# DriverAssignment5.py
# author: your name here
# proposed points: I propose this submission is worth X (out of 8) points

# This script creates an 8-puzzle problem and calls the graph search method on it
# also outputs statistics on how many nodes were searched and time spent


from EightPuzzle import *
from GraphSearch import *
from BFS import *
from DFS import *
from IDS import *

# create the problem model
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))  # requires 2 moves
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 0, 8))  # requires 3 moves
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 0, 7, 8, 6))  # requires 3 moves
#other examples of creating an 8-puzzle problem
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0)) #requires 12 moves
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0)) #start with solution
#eight_puzzle.shuffle(10) # make 10 moves to ensure the puzzle is in a solvable state, but mixed up a bit
#eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))  # requires 3 vs 7 nodes, works better on DFS
eight_puzzle = EightPuzzle((1, 2, 0, 4, 5, 3, 7, 8, 6))  # requires 4 vs indefinete nodes, works better on BFS
#eight_puzzle = EightPuzzle((1, 2, 0, 4, 5, 3, 7, 8, 6)) #start with solution

#Depth first search works better if the algorithm goes all the way down one side of the decision tree and the solution is within one of those nodes. May if the solution is further down the node.
#Breadth firest search works better if the relatively shallow and in the center of the graph. 

# search using Graph Search
# myGraphSearch = GraphSearch(eight_puzzle)
# result_node = myGraphSearch.search()
# 
# print("GRAPH SEARCH")
# 
# if (result_node is None):
#     print("No path found using graph search!")
# else:
#     print("Path:", result_node.path())
#     print("Path Cost:", result_node.path_cost)
#     print("Solution:", result_node.solution())
# print("Nodes searched with graph search:", myGraphSearch.nodesSearched)
# print("Time Spent with graph search:", myGraphSearch.timeSpent)
# 
# 
# print("==============")
# print("")
print("BREADTH FIRST SEARCH")

# search using BFS Search
myBFSSearch = BFS(eight_puzzle)
result_node = myBFSSearch.search()

if (result_node is None):
    print("No path found using tree search!")
else:
    print("Path:", result_node.path())
    print("Path Cost:", result_node.path_cost)
    print("Solution:", result_node.solution())
print("Nodes searched with BFS:", myBFSSearch.nodesSearched)

print("Time Spent with BFS:", myBFSSearch.timeSpent)
# 
# 
# print("==============")
# print("")
# print("DEPTH FIRST SEARCH")
# 
# #search using DFS Search
# myDFSSearch = DFS(eight_puzzle)
# result_node = myDFSSearch.search()
# 
# if (result_node is None):
#     print("No path found using DFS search!")
# else:
#     print("Path:", result_node.path())
#     print("Path Cost:", result_node.path_cost)
#     print("Solution:", result_node.solution())
# print("Nodes searched with DFS:", myDFSSearch.nodesSearched)
# print("Time Spent with DFS:", myDFSSearch.timeSpent)


print("==============")
print("")
print("ITERATIVE DEEPENING SEARCH")

#search using IDS Search
myIDSSearch = IDS(eight_puzzle)
result_node = myIDSSearch.search()

if (result_node is None):
    print("No path found using IDS search!")
else:
    print("Path:", result_node.path())
    print("Path Cost:", result_node.path_cost)
    print("Solution:", result_node.solution())
print("Nodes searched with IDS:", myIDSSearch.nodesSearched)
print("Time Spent with IDS:", myIDSSearch.timeSpent)


print("==============")