# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        # Here 1_1, 5_1, 5_2 and 5_3 are also subtrees whose child nodes are all same or null. 
        # "3 subtrees with 5 or null as node values" and "1 subtree as 1 or null as same values".
        # Again: Key here is each of these subtrees don't have to have the same value.
        
        self.ans = 0
        
        def dfs(node, parent):
            if not node:
                return True
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent
        dfs(root, None)
        
        return self.ans        