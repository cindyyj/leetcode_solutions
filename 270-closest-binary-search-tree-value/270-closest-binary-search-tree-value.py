# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        cur = root
        closest = cur.val

        while cur:
            closest = min(cur.val, closest, key = lambda x: abs(target-x))
            cur = cur.left if target < cur.val else cur.right
            # if cur.val > target:
            #     cur = cur.right
            # else:
            #     cur = cur.left
        
        return closest
        
        
#         def inorder(r):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
#         nums = inorder(root)
#         return min(nums, key = lambda x: abs(target - x))