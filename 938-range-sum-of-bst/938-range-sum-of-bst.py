# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
#         # BFS
        
#         total = 0
#         q = collections.deque([root])
        
#         while q:
#             node = q.popleft()
#             if not node:
#                 continue
#             if node.val > high:
#                 q.append(node.left)
#             elif node.val < low:
#                 q.append(node.right)
#             else:
#                 total += node.val
#                 q.append(node.left)
#                 q.append(node.right)
                
#         return total
        
        
        # DFS        
        if not root:
            return 0        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)        
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)      
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        
#         # BFS
        
#         from collections import deque
        
#         queue = deque([root])
#         total = 0
        
#         while queue:
#             node = queue.popleft()
#             if low <= node.val <= high:
#                 total += node.val
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             elif node.val < low: # must be on right
#                 if node.right:
#                     queue.append(node.right)
#             else: 
#                 if node.left:
#                     queue.append(node.left)
        
#         return total
                
                    
        
#         def inorder(root):
#             return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
#         nums = inorder(root)
        
#         total = 0
#         for _, n in enumerate(nums):
#             if low <= n <= high:
#                 total += n
        
#         return total