# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return root
        
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
            
            ans.append(max(level))
        
        return ans
        