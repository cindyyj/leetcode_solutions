"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        diameter = 0
        
        def dfs(r):
            # base case for leaf, first store the maximum depth, second is second maximum depth
            first = second = 0
            for child in r.children:
                depth = dfs(child)
                if depth > first:
                    first, second = depth, first
                elif depth > second:
                    second = depth
            
            nonlocal diameter
            diameter = max(diameter, first + second)
            return first + 1
        
        dfs(root)
        return diameter