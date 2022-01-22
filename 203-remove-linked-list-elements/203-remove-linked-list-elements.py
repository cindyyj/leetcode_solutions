# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Iterative
        # Time, O(n); S: O(1)
        # （迭代-单独处理头节点）

        while head and head.val == val:
            head = head.next
            
        if not head:
            return head
                
        pre, cur = head, head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur                
            cur = cur.next
            
        return head