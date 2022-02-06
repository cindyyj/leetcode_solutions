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
    def connect(self, root: 'Node') -> 'Node':
        # The algorithm is a BFS or level order traversal. 
        # We go through the tree level by level. node is the pointer in the parent level, tail is the tail pointer in the child level.
        # The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
        # Connect the tail with every one of the possible nodes in child level, update it only if the connected node is not nil.
        # Do this one level by one level. The whole thing is quite straightforward.

        if not root:
            return root
        
        from collections import deque
        
        queue = deque([root, None])
        
        while queue:
            node = queue.popleft()              

            if node is None: # end of curr level
                if len(queue) >= 1:
                    queue.append(None)

            else: # if node
                node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
  
         # if not root:
#             return root
        
#         from collections import deque
#         curr_level = deque([root, None])
        
#         while curr_level:
#             next_level = []
            
#             for _ in range(len(curr_level)):
                
#                 node = curr_level.pop()
#                 if not node:
#                     if len(next_level) != 0:
#                         next_level.append(None)
                
#                 else: 
#                     node.next = curr_level[0] # error, list index out of range!!

#                     if node.left:
#                         next_level.append(node.left)
#                     if node.right:
#                         next_level.append(node.right)
                    
#             curr_level = next_level
        
#         return root