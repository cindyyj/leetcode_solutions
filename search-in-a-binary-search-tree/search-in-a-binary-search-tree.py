# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative
        
        if not root:
            return None
        
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left

        
#         # recursive
#         if not root:
#             return None
        
#         if root.val == val:
#             return root
        
#         elif root.val < val:
#             return self.searchBST(root.right, val)
        
#         else:
#             return self.searchBST(root.left, val)
        
#         return None