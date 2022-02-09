# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def DFS(self,root,p,q):
        if root:
            if root in (None,p,q):
                return root
            l = self.DFS(root.left,p,q)
            r = self.DFS(root.right,p,q)
            return root if l and r else l or r        
        else:
            return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.DFS(root,p,q)    
    
    
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         # https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/
#         # 二叉树公共祖先专题
#         """
#         Using a bottom-up approach, we can improve over the top-down approach by avoiding traversing the same nodes over and over again.

#         We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent. The parent would then test its left and right subtree if each contain one of the two nodes. If yes, then the parent must be the LCA and we pass its parent up to the root. If not, we pass the lower node which contains either one of the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree does not contain either p or q) up.

#         Sounds complicated? Surprisingly the code appears to be much simpler than the top-down one.       
#         """   
        
#         if not root or root == p or root == q:
#             return root
        
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
        
#         if left and right:
#             return root
#         return left if left else right
        
#         # if root in (None, p, q): return root
#         # left, right = (
#         #     self.lowestCommonAncestor(kid, p, q)
#         #     for kid in (root.left, root.right))
#         # return root if left and right else left or right
#         # 时间复杂度 O(N) ： 其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
#         # 空间复杂度 O(N)  ： 最差情况下，递归深度达到 N ，系统使用 O(N)大小的额外空间。

# # 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
#         if not root:
#             return None        
        
#         if root == p or root == q: 
#             return root
        
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
        
#         if not left and not right: # if left is null and right is null
#             return
        
#         if not left: # left is null, on right side
#             return right
        
#         if not right: # right null, on left side
#             return left
        
#         return root # if left and right 

