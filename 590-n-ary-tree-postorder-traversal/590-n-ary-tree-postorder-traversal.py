"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        
        # perform dfs on the root and get the output stack
        self.dfs(root, ans)
        
        # return the output of all the nodes.        
        return ans
        
    def dfs(self, root, ans):
        
        if not root:
            return root
        
        # add all the children to the output
        for child in root.children:
            self.dfs(child, ans)
        
        # add root val later for postorder
        ans.append(root.val)