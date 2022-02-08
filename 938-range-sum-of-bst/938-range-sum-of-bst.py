# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        nums = inorder(root)
        
        total = 0
        for _, n in enumerate(nums):
            if low <= n <= high:
                total += n
        
        return total