# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             self.dfs(root.right, res)
#             res.append(root.val)
    
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.dfs(root, res)
#         return res

# iteratively        
    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]