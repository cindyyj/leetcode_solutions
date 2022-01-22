# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Iterative with dummy head
        
        if not head:
            return head
        
        dummy, dummy.next = ListNode(0), head
        
        pre, cur = dummy, head
        
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        
        return dummy.next
        
#         # Iterative
#         # Time, O(n); S: O(1)
#         # （迭代-单独处理头节点）

#         while head and head.val == val:
#             head = head.next
            
#         if not head:
#             return head
                
#         pre, cur = head, head.next
#         while cur:
#             if cur.val == val:
#                 pre.next = cur.next
#             else:
#                 pre = cur                
#             cur = cur.next
            
#         return head
    
        