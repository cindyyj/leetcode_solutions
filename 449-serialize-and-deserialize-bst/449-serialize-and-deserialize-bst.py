# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        # classic!!! 
        
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        
        return ' '.join(map(str, postorder(root)))
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        data = [int(x) for x in data.split(' ') if x]
        return self.decode(data)
        
    def decode(self, data, lower = float('-inf'), upper = float('inf')):

        if not data or data[-1] < lower or data[-1] > upper:
            return None

        val = data.pop()
        root = TreeNode(val)
        root.right = self.decode(data, val, upper)
        root.left = self.decode(data, lower, val)

        return root


        

# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/solution/xu-lie-hua-he-fan-xu-lie-hua-er-cha-sou-suo-shu-2/
    

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
