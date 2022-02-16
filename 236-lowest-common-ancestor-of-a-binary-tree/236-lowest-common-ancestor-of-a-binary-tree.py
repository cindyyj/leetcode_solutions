# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root in [None, p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left if left else right


# class Solution:

#     def DFS(self,root,p,q):
#         if root:
#             if root in (None,p,q):
#                 return root
#             l = self.DFS(root.left,p,q)
#             r = self.DFS(root.right,p,q)
#             return root if l and r else l or r        # else l or r same as return left if left else right
#         else:
#             return None
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         return self.DFS(root,p,q)    
    
    
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

"""
递归解析：
终止条件：
当越过叶节点，则直接返回 null ；
当 root 等于 p, q，则直接返回 rootroot ；
递推工作：
开启递归左子节点，返回值记为 left ；
开启递归右子节点，返回值记为 right ；
返回值： 根据 left 和 right ，可展开为四种情况；
当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null ；
当 left 和 right  同时不为空 ：说明 p, q 分列在 rootroot 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
当 left 和 right  不为空 ：p,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 pp ）；
p,q 两节点都在 root 的 右子树 中，此时的 rightright 指向 最近公共祖先节点 ；
当 left 不为空 ， right 为空 ：与情况 3. 同理；

作者：jyd
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""