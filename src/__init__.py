#! /usr/bin/env python
"""
Author: Jeremy M. Stober
Program: __INIT__.PY
Date: Thursday, May 17 2012
Description: A* search in Python.
"""

import heapq as hq

class pqueue:
    """
    A priority queue with fast member checking and variable tie
    breaking (LIFO or FIFO).
    """
    def __init__(self, ties = "LIFO"):
        self.cnt = 0
        self.heap = []
        self.set = set()
        self.ties = ties

    def push(self, pri, indx):
        hq.heappush(self.heap, (pri, self.cnt, indx))
        self.set.add(indx)
        if self.ties == "LIFO":
            self.cnt -= 1
        else: #FIFO
            self.cnt += 1

    def __contains__(self, indx):
        return indx in self.set

    def __len__(self):
        return len(self.heap)

    def pop(self):
        pri, cnt, indx = hq.heappop(self.heap)
        self.set.remove(indx)
        return indx

def reconstruct(partialmap, node):
    if partialmap.has_key(node):
        return reconstruct(partialmap, partialmap[node]) + [node]
    else:
        return [node]

def astar(neighbors, start, goal, hcost, dist):
    """
    neighbors: a dictionary that maps each node to a list of neighbors.
    start: the index of the start node.
    goal: the index of the goal node.
    hcost: heuristic cost function.
    """

    start_score = hcost(start,goal)
    openset = pqueue()
    closedset = set()

    openset.push(start_score, start)

    closedset = set()
    partialmap = {}
    gscore = {}
    fscore = {}
    fscore[start] = hcost(start,goal)

    while len(openset) > 0:

        # current lowest estimated cost node
        current = openset.pop()

        if current == goal: # finished - so build a map
            return reconstruct(partialmap, goal)

        closedset.add(current)
        for neighbor in neighbors[current]:

            if neighbor in closedset:
                continue

            tenative_gscore = gscore.get(current, 0) + dist[current,neighbor]

            if not neighbor in openset or tenative_gscore < gscore.get(neighbor,0):
                partialmap[neighbor] = current
                gscore[neighbor] = tenative_gscore
                fscore[neighbor] = gscore[neighbor] + hcost(neighbor, goal)
                openset.push(fscore[neighbor], neighbor)

    return False # bad result - no path found

if __name__ == '__main__':

    start = 0
    goal = 6

    # http://en.wikipedia.org/wiki/File:AstarExample.gif
    neighbors = {0:[1,2],
                 1:[3],
                 2:[4],
                 3:[6],
                 4:[5],
                 5:[6],
                 6:[]}

    costs = {(0,1):2,
             (0,2):1.5,
             (1,3):3,
             (2,4):2,
             (3,6):2,
             (4,5):4,
             (5,6):4}

    def hcost(indx1,indx2): # makes astar == dijkstra's algorithm
        return 0.0

    print astar(neighbors, start, goal, hcost, costs)
