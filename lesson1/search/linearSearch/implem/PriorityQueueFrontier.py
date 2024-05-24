import heapq
import sys
from abc import ABC, abstractmethod

sys.path.append("/lesson1/search/linearSearch") 
# The priority queue orders the nodes based on a heuristic, typically the estimated cost to reach the goal from the current node.
import heapq
from abc import ABC, abstractmethod

from abstract.Frontier import Frontier


class PriorityQueueFrontier(Frontier):
    def __init__(self):
        self.frontier = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = 0

    def add(self, node, priority):
        # Convert node to tuple if it is not already
        node_tuple = tuple((tuple(sub) if isinstance(sub, list) else sub) for sub in node)
        # If the node is already in the frontier, mark it as removed
        if node_tuple in self.entry_finder:
            self.remove_node(node_tuple)
        count = self.counter
        entry = [priority, count, node_tuple]
        self.entry_finder[node_tuple] = entry
        heapq.heappush(self.frontier, entry)
        self.counter += 1

    def remove(self):
        while self.frontier:
            priority, count, node = heapq.heappop(self.frontier)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return node
        raise KeyError('pop from an empty priority queue')

    def remove_node(self, node):
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED

    def is_empty(self):
        return not self.frontier