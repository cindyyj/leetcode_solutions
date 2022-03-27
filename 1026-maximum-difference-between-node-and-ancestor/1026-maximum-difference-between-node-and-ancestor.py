# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        res = 0
        
        def dfs(node, max_val, min_val):
            if not node:
                return
            
            cur_max, cur_min = max(max_val, node.val), min(min_val, node.val)
            nonlocal res
            res = max(res, cur_max - cur_min)            
            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)
        
        dfs(root, 0, 10**5)
        return res