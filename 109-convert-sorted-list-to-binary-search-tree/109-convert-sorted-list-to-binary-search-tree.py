# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def list_to_vals(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        vals = self.list_to_vals(head)
        
        # 108, sorted array to BST
        def dfs(l, r):

            if l > r:
                return None

            # mid for root
            mid = (l + r) // 2
            root = TreeNode(vals[mid])
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root
        
        return dfs(0, len(vals) - 1)
        
            
            
            
