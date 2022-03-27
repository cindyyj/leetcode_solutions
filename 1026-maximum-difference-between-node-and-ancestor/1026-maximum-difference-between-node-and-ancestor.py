# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        
        def dfs(node, max_val, min_val):
            if not node:
                nonlocal res
                res = max(res, max_val - min_val)
                return
                
            dfs(node.left, max(max_val, node.val), min(min_val, node.val))
            dfs(node.right, max(max_val, node.val), min(min_val, node.val))
        
        dfs(root, 0, 10**5)
        return res