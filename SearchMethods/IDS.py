"""
Iterative Deepening Search (ids)

implements a Iterative Deepening Search

"""

from collections import deque
from Node import *
import time

class IDS():
    """
    Creates a new Graph Search object

    model: a Problem model of the environment
    """
    def __init__(self, problem):
        # save the params
        self.problem = problem
        self.nodesSearched = 0
        self.timeSpent = 0

    """
    Searches for a path from the start state to a goal state using the Problem given
    to the constructor
    """
    def search(self):
        return self.ids(self.problem.initial)

    """
    Conducts Depth First Graph Search from a given start state.
    state: the start state for the search
    """
    def ids(self, startState):
        startTime = time.time()
        
        for l in range(33):
            root = Node(startState)
            frontier = deque([root])
            while len(frontier) > 0:
                #print(frontier)
                node = frontier.pop()
                #print("Current Node", node)
                #print(node)
                self.nodesSearched += 1
                #print("Current node", node)
            
                if self.problem.goal_test(node.state):
                    self.timeSpent = time.time() - startTime  
                    return node   

            # expand node in frontier
                for action in self.problem.actions(node.state):
                    nextState = self.problem.result(node.state, action)
                    child = Node(state=nextState, parent=node,
                                  path_cost=self.problem.path_cost(node.path_cost, node.state, action, nextState),
                                  action=action)
                
                #print("The child",child)

                    if child.depth <= l and child not in frontier:
                        frontier.append(child)
                  
                    #print("child cost",child.path_cost)
            l = l + 1
            
        self.timeSpent = time.time() - startTime   
    

        return None

        




