import sys

sys.path.append("/lesson1/search/linearSearch") 
from abstract.Frontier import Frontier


class StackFrontier(Frontier):
    def __init__(self):
        self.frontier=[]

    def add(self,node):
        self.frontier.append(node)
    
    def remove(self):
        # since we're using stack here, the removal should follow the Last-in First-out rule
        return self.frontier.pop() 
    
    