# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
        # recursive 3 line
        # The assignment operation = is performed after the RHS of the statement is evaluated. 
        # Here, the RHS (right hand side) of statement root.left, root.right = self.invertTree(root.right), self.invertTree(root.left) 
        # is an implicit tuple object that has 2 elements namely self.invertTree(root.right) and self.invertTree(root.left). 
        # Only after both of these function calls are evaluated, the assignment operation is performed.
        # Because of this order, we don't lose any information.
        
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
        
#         # recursive
#         if not root:
#             return root
        
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root       
        