import sys
from abc import ABC, abstractmethod
from collections import deque


# this is going to be the abstract Frontier Class
class Frontier(ABC):
    @abstractmethod
    def add(self, node):
        pass
    @abstractmethod
    def remove(self):
        pass
