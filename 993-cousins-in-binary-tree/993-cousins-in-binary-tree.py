# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # classic!
        # https://leetcode.com/problems/cousins-in-binary-tree/discuss/299889/Python-BFS-solution        

        # Concept is to store the parent and level information here while performing BFS 
        # and break early once you have both x and y in nodeMap
        # no need to perform the BFS till the very end which is making it run slow. 
        
        # application of defaultdict!!!
        
        
#         from collections import deque, defaultdict        
#         q = deque()
#         nodeMap = defaultdict(list) # key-value pairs into a dictionary of lists
        
#         # node, level, parent
#         q.append((root, 0, 0))
        
#         while q: 
#             if x in nodeMap and y in nodeMap: # if x, y already in the nodeMap keys!
#                 break
                
#             node, level, parent = q.popleft()
#             nodeMap[node.val] = [level, parent]
            
#             if node.left:
#                 q.append((node.left, level + 1, node.val))
#             if node.right:
#                 q.append((node.right, level + 1, node.val))
                
#         # if same level, not same parent
#         if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][0] != nodeMap[y][0]:
#             return True
        
#         return False
    
        q = collections.deque()
        nodeMap = collections.defaultdict()
        q.append((root, 0, 0))
        
        while q:
            if x in nodeMap and y in nodeMap:
                break
            node, level, parent = q.popleft()
            nodeMap[node.val] = [level, parent]

            if node.left:
                q.append((node.left, level+1, node.val))

            if node.right:
                q.append((node.right, level+1, node.val))
        
        if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][1] != nodeMap[y][1]:
            return True
        return False