# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0
        
        def dfs(node):
            if not node:
                return 0 
            nonlocal d 
            
            l = dfs(node.left)
            r = dfs(node.right)
            d = max(d, l + r)
            
            return max(l, r) + 1
        
        dfs(root)
        return d
        
        
    # 错误解答： 最大直径是左子树和右子树的最大深度之和，
    # 但是万一最大直径没有经过根节点呢？
    # 所以说对于树中的每一个结点，都要把它视为根节点，然后比较所有结点的左子树和右子树的最大深度之和，取其中的最大值。
    
    # classic!!!
    
    # https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/hot-100-9er-cha-shu-de-zhi-jing-python3-di-gui-ye-/

    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter

        
    def depth(self, root):
        
        if not root:
            return 0
        
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.diameter = max(self.diameter, l+r)

        '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值'''
        
        # 返回的是高度
        return max(l,r) + 1
  