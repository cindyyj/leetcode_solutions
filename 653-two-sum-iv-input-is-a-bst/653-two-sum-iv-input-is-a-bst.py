# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, seen, k):
        if not root:
            return False
        
        complement = k- root.val
        if complement in seen:
            return True
        seen.add(root.val)
        
        return self.dfs(root.left, seen, k) or self.dfs(root.right, seen, k)
    
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs(root, set(), k)
        # hash set, space O(n), Time o(n)
        # didn't use the feature of BST
        


#     # BST returns a sorted inorder array, then binary search
#     def inorder(self, root, nums):
#         if not root:
#             return
        
#         self.inorder(root.left, nums)
#         nums.append(root.val)
#         self.inorder(root.right, nums)
        
        
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         nums = []
#         self.inorder(root, nums)
        
#         left, right = 0, len(nums)-1
#         while left < right:
#             total = nums[left] + nums[right]
#             if total == k:
#                 return True
#             elif total < k:
#                 left += 1
#             else: 
#                 right -= 1
        
#         return False