# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # level-traverse
        # https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/dai-ma-sui-xiang-lu-wo-yao-da-shi-ge-er-cbxt1/
        # # 认准「代码随想录」，学习算法不迷路！

        # 不少同学对二叉树的递归与非递归遍历，
        # 学会二叉树的层序遍历，可以一口气打完以下十题：

        # 102.二叉树的层序遍历
        # 107.二叉树的层次遍历II
        # 199.二叉树的右视图
        # 637.二叉树的层平均值
        # 429.N叉树的前序遍历
        # 515.在每个树行中找最大值
        # 116.填充每个节点的下一个右侧节点指针
        # 117.填充每个节点的下一个右侧节点指针II
        # 104.二叉树的最大深度
        # 111.二叉树的最小深度

        # 作者：carlsun-2
        # 链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/dai-ma-sui-xiang-lu-wo-yao-da-shi-ge-er-cbxt1/
        
        if not root:
            return 0 
        
        from collections import deque
        queue = deque([root])
        ans = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(level)
        
        return len(ans)  # how many levels traversed
                
        
#         # recursive
#         if not root:
#             return 0
        
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        