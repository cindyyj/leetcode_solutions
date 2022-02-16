# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        if not root:
            return root
        
        # edge case
        if len(nodes)==1:
            return nodes[0]
        
        nodes = set(nodes)
        if root in nodes:
            return root
        
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        
        if left and right:
            return root
        return left or right
    
    # same logic as L235, if some nodes in left subtree, others in right subtree, LCA must be root   
    # else all nodes in one side of the tree, so the LCA is what ever returned from left and right that is not None
