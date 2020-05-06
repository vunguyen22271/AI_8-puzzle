import numpy as np
import itertools
from copy import deepcopy
list2d = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
merged = list(itertools.chain.from_iterable(list2d))


class Node:
    state = None
    parent = None
    path_cost = None
    action = None


class Problem:
    col = {0: 'RIGHT', 2: 'LEFT', 1: ['LEFT', 'RIGHT']}
    row = {0: 'DOWN', 2: 'UP', 1: ['UP', 'DOWN']}
    step_cost = 1

    state = np.array([[3, 1, 2],
                      [6, '', 8],
                      [7, 5, 4]])
    goal = np.array([['', 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]])

    def returnBlankIndex(self, node):
        return np.where(node.state == '')

    def returnActionArray(self, node):
        index = self.returnBlankIndex(node)
        rowindex = index[0].item()
        colindex = index[1].item()
        action = []
        action.append(self.row[rowindex])
        action.append(self.col[colindex])
        action = list(itertools.chain.from_iterable(action))
        return action

    def initial_state(self):
        node = Node
        node.state = self.state
        node.action = self.returnActionArray(node)
        node.path_cost = 0
        return node

    def goal_test(self, node):
        # for i in range(3):
        #     for j in range(3):
        #         if self.goal[i][j] != node.state[i][j]:
        #             return 0
        # return 1
        check = node.state == self.goal
        if False in check:
            return 0
        else:
            return 1
    # Viet ham Result child state

    def result(self, node, action, explored, child):
        index = self.returnBlankIndex(node)
        rowBlankindex = index[0].item()
        colBlankindex = index[1].item()
        
        if action == 'UP':
            rowindex = rowBlankindex - 1
            colindex = colBlankindex
        elif action == 'DOWN':
            rowindex = rowBlankindex + 1
            colindex = colBlankindex
        elif action == 'LEFT':
            rowindex = rowBlankindex
            colindex = colBlankindex - 1
        elif action == 'RIGHT':
            rowindex = rowBlankindex
            colindex = colBlankindex + 1
        print('1:')
        print(node.state)
        print(explored)
        print(child.state)
        print('\n')
        #node.state[rowindex][colindex], node.state[rowBlankindex][colBlankindex] = node.state[rowBlankindex][colBlankindex], node.state[rowindex][colindex]
        node.state[0][0] = 10
        print('2:')
        print(node.state)
        print(explored)
        print(child.state)
        print('\n')
        return node.state


def child_node(problem, parent, action):
    child = Node()
    child.parent = parent
    child.action = action  # child chua action cua cha
    child.state = problem.result(parent, action)
    child.path_cost = parent.path_cost + problem.step_cost
    return child


def checkInExplored(explored, node):
    if node in explored:
        return 1
    else:
        return 0


def checkInFrontier(frontier, node):
    lenFrontier = len(frontier)
    i = 0
    for i in range(lenFrontier):
        check = node.state == frontier[i].state
        if check == True:
            return 1
    return 0


def UCS(problem):
    node = Node()
    node = problem.initial_state()
    frontier = [node]
    explored = []
    while(1):
        if len(frontier) <= 0:
            return 0
        else:
            min_path_cost = 1000000
            indexPop = int()
            for checkNode in frontier:
                if(checkNode.path_cost < min_path_cost):
                    indexPop = frontier.index(checkNode)
                    min_path_cost = checkNode.path_cost
            #node = frontier.pop(indexPop)
            node = frontier[indexPop]
            frontier.remove(frontier[indexPop])
            #print(node.state)
        if(problem.goal_test(node) == 1):
            return "Ra dap an"
        else:
            explored.insert(len(explored),node.state)

        for action in problem.returnActionArray(node):
            node.state[0][0] = 0
            print('Lá:')
            print(node.state)
            print(explored)
            print('\n')
            child = Node()
            child.parent = node
            child.action = action  # child chua action cua cha
            child.state = problem.result(node, action, explored, child)
            node.state[0][0] = 0
            print('Lást:')
            print(node.state)
            print(explored)
            print(child.state)
            print('\n')
            child.path_cost = node.path_cost + problem.step_cost
            # check state
            if checkInFrontier(frontier, node) == 0 and checkInExplored(explored, child.state) == 0:  # error
                frontier.append(child)
            elif checkInFrontier(frontier, node) == 1:
                print(0)


problem = Problem()
node = Node()
node = problem.initial_state()

UCS(problem)