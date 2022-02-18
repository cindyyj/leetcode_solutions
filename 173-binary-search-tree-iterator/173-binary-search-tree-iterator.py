# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):

        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest element in the BST
        self.index = -1

        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)
    
#     def __init__(self, root: Optional[TreeNode]):
#         self.nodes = [] # Array containing all the nodes in the sorted order
#         self.index = -1 #  Pointer to the next smallest element in the BST
#         self._inorder(root) # Call to flatten the input binary search tree

#     def _inorder(self, root):
#         return self._inorder(root.left) + [root.val] + self._inorder(root.right) if root else []
        
#     def next(self) -> int:
#         self.index += 1
#         return self.nodes[self.index]

#     def hasNext(self) -> bool:
#         return self.index + 1 < len(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()