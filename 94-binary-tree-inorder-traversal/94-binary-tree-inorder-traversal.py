# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def dfs(self, root, res):
    #     if root:
    #         self.dfs(root.left, res)
    #         res.append(root.val)
    #         self.dfs(root.right, res)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        
        # res = []
        # self.dfs(root, res)
        # return res