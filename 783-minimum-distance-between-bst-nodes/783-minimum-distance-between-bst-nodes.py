# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        nums = inorder(root)
        min_diff = float('inf')
        
        for i in range(1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - 1])
            
        return min_diff