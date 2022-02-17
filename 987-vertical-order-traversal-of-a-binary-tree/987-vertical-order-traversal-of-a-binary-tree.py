# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # 987 different from 314
        
        d = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                d[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        res = []
        for col in sorted(d.keys()):
            # sort first by 'row', then by 'value', in ascending order
            res.append([val for row, val in sorted(d[col])])
        
        return res