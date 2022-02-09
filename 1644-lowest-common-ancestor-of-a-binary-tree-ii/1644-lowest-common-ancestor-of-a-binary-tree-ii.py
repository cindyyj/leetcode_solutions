# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/discuss/934848/Python-BFS-and-DFS-methods
        
        self.existp = False
        self.existq = False
        
        ans = self.dfs(root, p, q)
        
        return ans if (self.existp and self.existq) else None
        
    
    def dfs(self, node, p, q):
        if not node:
            return None
        # traverse children
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        if node == p:
            self.existp = True
            return node
        
        if node == q:
            self.existq = True
            return node
        
        if left and right:
            return node
        
        return left or right
        
        
            
