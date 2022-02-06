# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        # 102的写法 + 标记位的常规写法
        
        queue = collections.deque([root])
        flag = 0
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
                
            if flag % 2 == 0:
                ans.append(level)
            else:
                ans.append(level[::-1])
            
            flag += 1
                
        return ans
        