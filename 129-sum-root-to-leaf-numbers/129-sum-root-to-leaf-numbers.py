# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(r, prev):
            if not r:
                return 0
            total = prev * 10 + r.val
            if not r.left and not r.right:
                return total
            else:
                return dfs(r.left, total) + dfs(r.right, total)
        
        return dfs(root, 0)
    
    """
    时间复杂度：O(n)，其中 n 是二叉树的节点个数。对每个节点访问一次。
    空间复杂度：O(n)，其中 n 是二叉树的节点个数。空间复杂度主要取决于递归调用的栈空间，递归栈的深度等于二叉树的高度，
    最坏情况下，二叉树的高度等于节点个数，空间复杂度为 O(n)。

    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
    """