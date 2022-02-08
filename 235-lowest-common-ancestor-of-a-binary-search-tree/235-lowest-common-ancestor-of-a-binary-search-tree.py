# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ((root.val - p.val) * (root.val - q.val)) > 0 means p, q must be on same side of tree
        while ((root.val - p.val) * (root.val - q.val)) > 0:
            root = root.left if p.val < root.val else root.right
        
        return root    
        
#         # method 1
#         p_val = p.val
#         q_val = q.val
#         root_val = root.val
        
#         if p_val > root_val and q_val > root_val:
#             # error, forget to add return statement
#             return self.lowestCommonAncestor(root.right, p, q)
#         elif p_val < root_val and q_val < root_val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         else:
#             return root        