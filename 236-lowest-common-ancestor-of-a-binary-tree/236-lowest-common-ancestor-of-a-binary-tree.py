# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root in (None, p, q): return root
        # left, right = (
        #     self.lowestCommonAncestor(kid, p, q)
        #     for kid in (root.left, root.right))
        # return root if left and right else left or right
        # 时间复杂度 O(N) ： 其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
        # 空间复杂度 O(N)  ： 最差情况下，递归深度达到 N ，系统使用 O(N)大小的额外空间。

# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
        if not root:
            return None        
        
        if root == p or root == q: 
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left and not right: # if left is null and right is null
            return
        
        if not left: # left is null, on right side
            return right
        
        if not right: # right null, on left side
            return left
        
        return root # if left and right 

