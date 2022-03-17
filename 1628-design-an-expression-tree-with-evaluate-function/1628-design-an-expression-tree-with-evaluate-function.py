import abc 
from abc import ABC, abstractmethod 

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        else:    
            return self.left.evaluate() // self.right.evaluate()
            
    

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur     



# """
# This is the interface for the expression tree Node.
# You should not remove it, and you can define some classes to implement it.
# """

# class Node(ABC):
#     # @abstractmethod
#     # define your fields here
    
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
#     def evaluate(self) -> int:
#         if not self.left and not self.right:
#             return self.val
#         else:
#             op = self.val
#             left_val = self.left.evaluate()
#             right_val = self.right.evaluate()
#             if op == "+":
#                 return left_val + right_val
#             elif op == "-":
#                 return left_val - right_val
#             elif op == "*":
#                 return left_val * right_val            
#             else: 
#                 return left_val // right_val  
            
#     def gatherAttrs(self):
#         return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())
    
#     def __str__(self):
#         return self.__class__.__name__ + "{" +"{}".format(self.gatherAttrs())
    

# """    
# This is the TreeBuilder class.
# You can treat it as the driver code that takes the postinfix input
# and returns the expression tree represnting it as a Node.
# """

# class TreeBuilder(object):
#     def buildTree(self, postfix: List[str]) -> 'Node':
#         stack = []
#         for t in postfix:
#             if t.isnumeric():
#                 stack.append(Node(int(t)))
#             else:
#                 right = stack.pop()
#                 left = stack.pop()
#                 stack.append(Node(t, left, right))
                
#         return stack.pop()
        
		
# """
# Your TreeBuilder object will be instantiated and called as such:
# obj = TreeBuilder();
# expTree = obj.buildTree(postfix);
# ans = expTree.evaluate();
# """
        