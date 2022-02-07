# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
#     def inorder(self, root, nums):
#         if not root:
#             return 
        
#         self.inorder(root.left, nums)
#         nums.append(root.val)
#         self.inorder(root.right, nums)
        
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         nums = []
#         self.inorder(root, nums)
        
#         return nums[k-1]
    

    # leetcode official solution
    # great overview of tree reversal
    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
    # Time complexity : O(N) to build a traversal.
    # Space complexity : O(N) to keep an inorder traversal.
    
    # follow up!!!
    # What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
    # How would you optimize the kthSmallest routine?
    # insert/delete a node into BST, time: O(h), h is height of binary tree. H = log(n) for balanced tree, H=N for skewed tree
    # O (h) time for insert and delete
    # o (k) for search kth smallest
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return inorder(root)[k - 1]
