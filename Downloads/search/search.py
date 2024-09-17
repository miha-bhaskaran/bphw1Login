# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # using stack => pop off first element and put into stack (mark visit?), put neightbors into stack , then pop off 
    # second element and mark visited, then visit b's children

    # get successor => (successor, action, stepCost)

    # print("Start:", problem.getStartState()) => (5,5)
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState())) => bool
    # print("Start's successors:", problem.getSuccessors(problem.getStartState())) => [((5, 4), 'South', 1), ((4, 5), 'West', 1)]

    stack = util.Stack()
    visit = set()
    starting = problem.getStartState()

    # stack = [(node position), [directions]]

    stack.push((starting, []))
    # (5,5) []

    while stack:
        node, direction = stack.pop()
        # (5,5) []
        visit.add(node)
        if problem.isGoalState(node):
            return direction
        else:
            children =  problem.getSuccessors(node)
            for child in children:
                #child => [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
                nodeC, directionC, costC = child
                if nodeC not in visit:
                    #visit.add(nodeC)
                    stack.push((nodeC, direction + [directionC]))








def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # queue
    # put first elem in queue, then pop, and look at neighbors, insert all neighbors into queie order does not matter
    # pop off b and push all neighbors of b into queue, then take out c and put f and g into quue1q()
    q = util.Queue()
    visit = set()
    starting = problem.getStartState()
    q.push((starting, []))
    while q:
        node, direction = q.pop()
        visit.add(node)
        if problem.isGoalState(node):
            return direction
        children =  problem.getSuccessors(node)
        for child in children:
            #child => [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
            nodeC, directionC, costC = child
            if nodeC not in visit:
                visit.add(nodeC)
                q.push((nodeC, direction + [directionC]))






def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    #visitned 
    # start with s and visit and calculate totla cost of the neighbors, visit cheapest, then mark a as vistieds

    q = util.PriorityQueue()
    costs = {}
    # visit = set()
    starting = problem.getStartState()
    q.push((starting, [], 0), 0)
    costs[starting] = 0
    # {(5,5): 0, }
    # push(self, item, priority):
    while not q.isEmpty():
        node, direction, cost = q.pop()
        # visit.add(node)
        if problem.isGoalState(node):
            return direction
        children = problem.getSuccessors(node)
        for child in children:
            next_node, action, step_cost = child
            new_cost = cost + step_cost
            if next_node not in costs or new_cost < costs[next_node]:
                costs[next_node] = new_cost
                q.push((next_node, direction + [action], new_cost), new_cost)
    return []


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    q = util.PriorityQueue()
    costs = {}
    visit = set()
    starting = problem.getStartState()
    q.push((starting, [], 0), 0)
    costs[starting] = 0
    # {(5,5): 0, }
    # push(self, item, priority):

    while not q.isEmpty():
        node, direction, cost = q.pop()
        if problem.isGoalState(node):
            return direction
        visit.add(node)
        children = problem.getSuccessors(node)
        for child in children:
            next_node, action, step_cost = child
            new_cost = cost + step_cost
            if next_node not in costs or new_cost < costs[next_node]:
                costs[next_node] = new_cost
                priority = new_cost + heuristic(next_node, problem)
                q.push((next_node, direction + [action], new_cost), priority)
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
