# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # Nice for recursion version, but BFS might be more simple and easy to understand. Hope it helps:
        # Moreover, for this problem BFS will generally out-perform DFS especially on larger trees. (The OP's solution being DFS.)
        # https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36060/3-lines-in-Every-Language
        
        if not root:
            return 0
        
        depth = 0
        curr_level = [root]
        
        while curr_level:
            depth += 1
            next_level = []
            
            for node in curr_level:
                left = node.left
                right = node.right
                # 如果当前节点的左右孩子都为空，直接返回最小深度
                if not left and not right:
                    return depth
                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)
            
            curr_level = next_level
        
        return depth