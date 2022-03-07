# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(r):
            return inorder(r.left) + [r] + inorder(r.right) if r else []
        
        trees = inorder(root)
        s_trees = sorted(trees, key=lambda x: x.val)
        p, q = [trees[i] for i in range(len(trees)) if trees[i] != s_trees[i]]
        p.val, q.val = q.val, p.val                                                                        