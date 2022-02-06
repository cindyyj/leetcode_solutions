# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/dai-ma-sui-xiang-lu-wo-yao-da-shi-ge-er-cbxt1/
        # same level traversal 
        # reverse the output (102. level order traversal)
        
        # Time, O(n), traverse tree once
        # space, O(n), maximum queue is n/2 (in the bottom)
        
        if not root:
            return root
        
        from collections import deque
        
        queue = deque([root])
        res = [] # alternatively, This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. 
        # The only difference will be that instead of appending the current level at the end, we will append the current level at the beginning of the result list.
        # basically set res as a deque(), and res.appendleft(level)
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(level)
        
        return res[::-1]