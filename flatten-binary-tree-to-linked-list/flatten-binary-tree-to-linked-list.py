# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        queue = collections.deque([])
        
        self.dfs(root, queue)
        
        # cur begins from head
        cur = queue.popleft()
        cur.left = None
        
        # 遍历链表，将链表中的TreeNode节点前后串联起来
        while queue:
            nextnode = queue.popleft()
            nextnode.left = None
            cur.right = nextnode
            cur = nextnode
    
        return root
    
    def dfs(self, root, queue):
        # 前序遍历整棵二叉树，并将遍历的结果放到数组中
        if not root:
            return root
        queue.append(root)
        self.dfs(root.left, queue)
        self.dfs(root.right, queue)
        
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/dong-hua-yan-shi-si-chong-jie-fa-114-er-cha-shu-zh/
