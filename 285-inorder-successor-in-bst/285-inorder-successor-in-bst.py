# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def inorder(r):
            return inorder(r.left) + [r] + inorder(r.right) if r else []
        
        lst = inorder(root)
        for i in range(len(lst)):
            if lst[i].val == p.val and i < len(lst) - 1:
                return lst[i + 1]
            
        return None
        
        
        
        # if not root: 
        #     return None
        # if root.val > p.val: 
        #     return self.inorderSuccessor(root.left,p) or root 
        # return self.inorderSuccessor(root.right,p)
        
        
        # # BST
        # succ = None
        # while root:
        #     if p.val < root.val:
        #         succ = root
        #         root = root.left
        #     else:
        #         root = root.right
        # return succ    

    """
    What an amazing solution !! Below is version of predecessor inspired by this. Took me a bit to understand the logic behind how successor and predecessor works with this logic. For people like me :) , below is a little explanation that might help understand.

Inorder Successor:
First of all, what is inorder successor ?

It is the immediately bigger node than current node. If a node has right subtree, it is the smallest node found in the right subtree.
If the right subtree is null, it is the last node whose left subtree you are under.
How the algorithm finds it ?
On equality of the value whose inorder successor we are after, it makes it go to the right subtree. As all elements in the right subtree are larger than the current node, from that point onward the algorithm will be drawn towards finding the smallest value in right subtree. As we keep traversing down smaller nodes, we modify value of successor.

Inorder Predecessor
It is pretty much the same concept as successor.

If the left subtree exist, predecessor is the largest node found in left subtree.
If the left subtree does not exist, it is the last node whose right subtree the node is under.

How the algorithm finds it ?
On equality of the value whose inorder predecessor we are after, it makes traversal go to the left subtree. As all elements in leftsubtree are smaller than the node's value, algorithm will be drawn towards the largest value in that subtree. As we keep going right, we update the predecessor.
    
    """