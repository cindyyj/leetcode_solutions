# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def inorder(root):
            return (inorder(root.left) +
                    [root.val] +
                    inorder(root.right)) if root else []
        
        nums1 = inorder(root1)
        nums2 = inorder(root2)
        
        l, r = 0, len(nums2) - 1
        
        while l < len(nums1) and r >= 0:
            total = nums1[l] + nums2[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return True
        
        return False