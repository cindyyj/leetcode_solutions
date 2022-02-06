"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        ans =[]
        
        # perform dfs on the root and get the output stack
        self.dfs(root, ans)
        
        # return the output of all the nodes.
        return ans
    
    def dfs(self, root, ans):
        
        # If root is none return 
        if not root:
            return root
        
        # for preorder we first add the root val
        ans.append(root.val)
        
        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, ans)

       