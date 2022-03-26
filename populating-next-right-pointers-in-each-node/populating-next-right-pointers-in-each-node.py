"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space        
        if not root:
            return root
        
        from collections import deque 
        queue = deque([root])
        queue.append(None)
        
        while queue:
            
            node = queue.popleft()
            if node != None:
                node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else: # Upvoted for your brilliant usage of None to demarcate the levels!
                if len(queue) > 0: # finish traverse current level, next level fully populated, mark end with None
                    queue.append(None)
        
        return root