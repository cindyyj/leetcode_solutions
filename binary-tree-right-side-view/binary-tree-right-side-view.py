# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # deque来自collections模块，不在力扣平台时，需要手动写入
        # 'from collections import deque' 导入
        # deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度
        # 链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/dai-ma-sui-xiang-lu-wo-yao-da-shi-ge-er-cbxt1/

        if not root:
            return root
        
        from collections import deque
        queue, ans = deque([root]), []
        
        while queue:
            
            # 每次都取最后一个node就可以了
            right = queue[-1]
            ans.append(right.val)

            # 执行这个遍历的目的是获取下一层所有的node
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans

         