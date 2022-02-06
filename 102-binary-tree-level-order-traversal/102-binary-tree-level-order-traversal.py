# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # classic 
        # deque, double ended queue
        
        if not root:
            return []
        
        from collections import deque
        queue, ans = deque([root]), []
        
        while queue:
            
            level = []
            # current level
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            # add all nodes in the curr level 
            ans.append(level)
            
        return ans