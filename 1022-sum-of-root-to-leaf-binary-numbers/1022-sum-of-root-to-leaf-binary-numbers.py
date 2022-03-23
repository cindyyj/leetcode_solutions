# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(r, curr):
            nonlocal root_to_leaf
            if r:
                curr = curr << 1 | r.val
                # if leaf, update root_to_leaf
                if not (r.left or r.right):
                    root_to_leaf += curr
                
                preorder(r.left, curr)
                preorder(r.right, curr)
         
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf        