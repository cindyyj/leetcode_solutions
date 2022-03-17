import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    # @abstractmethod
    # define your fields here
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def evaluate(self) -> int:
        if not self.left and not self.right:
            return self.val
        else:
            op = self.val
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            if op == "+":
                return left_val + right_val
            elif op == "-":
                return left_val - right_val
            elif op == "*":
                return left_val * right_val            
            else: 
                return left_val // right_val  
            
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())
    
    def __str__(self):
        return self.__class__.__name__ + "{" +"{}".format(self.gatherAttrs())
    

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for t in postfix:
            if t.isnumeric():
                stack.append(Node(int(t)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(t, left, right))
                
        return stack.pop()
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        