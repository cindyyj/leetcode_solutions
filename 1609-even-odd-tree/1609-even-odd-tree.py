# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        # BFS, level order traversal 
        
        from collections import deque
        
        queue = deque([root])
        even_level = True
        
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                
                if even_level:
                    if val % 2 == 0: return False
                    if prev and prev.val >= val: return False
                else:
                    if val % 2 == 1: return False
                    if prev and prev.val <= val: return False
                
                prev = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            even_level = not even_level
        
        return True    