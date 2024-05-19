
import sys
from abc import ABC, abstractmethod
from collections import deque

sys.path.append("/lesson1/search/linearSearch") 
from abstract.Frontier import Frontier


class QueueFrontier(Frontier):

    def __init__(self):
        # Create an empty deque
        self.frontier=deque()

    def add(self,node):
        # Adds node to the right end
        self.frontier.append(node)

    def remove(self):
        # since we're using Queue here, we follow First-in First-out ruke
        self.frontier.popleft()