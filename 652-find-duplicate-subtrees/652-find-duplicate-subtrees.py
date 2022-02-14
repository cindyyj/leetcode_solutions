# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
For those who're confused why pre and post order works but not in order. I think this clears my confusion: https://leetcode.com/problems/find-duplicate-subtrees/discuss/106011/Java-Concise-Postorder-Traversal-Solution/108467. 
To be brief, it's because inorder can create same serialization for symmetric trees.
"""

class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            if not root:
                return "null"
            # important to add space between nodes!!!
            key = str(root.val) + ' ' + dfs(root.left) + ' ' + dfs(root.right)
            hashmap[key].append(root)
            return key
        
        hashmap = defaultdict(list)
        dfs(root)
        return [hashmap[i][0] for i in hashmap if len(hashmap[i]) > 1 ]
            


    
#     def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
#         # Concept - We can use a hashmap to store the all the trees and their roots
#         # Also advantage of using hashmap is you can easily find for the repeated
#         # or duplicate trees
#         hashmap = {}
#         res = []
#         self.solve(root, hashmap)

#         # Once the hashmap is built, we can just travserse through the values 
#         # and find out the values that are greater than 1 are repeated
#         for val, node in hashmap.values():
#             if val > 1:
#                 res.append(node)
#         return res
    
#     def solve(self, root, hashmap):
#         if not root:
#             return 'X'
        
#         left = self.solve(root.left, hashmap)
#         right = self.solve(root.right, hashmap)
        
#         # Pre-order tree representation for storing the tree
#         temp = str(root.val) + ' ' + left + ' ' + right
        
#         # Check if it is already in hashmap
#         if temp not in hashmap:
#             hashmap[temp] = [1, root]
        
#         else:
#             hashmap[temp][0] += 1
            
#         return temp