# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursive solution has O(n) memory complexity as it will consume memory on the stack up to the height of binary tree h.
    # It will be O(log n) for a balanced tree and in the worst case can be O(n).
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)
    
    def isValid(self, node, lower = float('-inf'), upper = float('inf') ):
        
        if not node: 
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not self.isValid(node.right, val, upper):
            return False
        
        if not self.isValid(node.left, lower, val):
            return False
        
        return True