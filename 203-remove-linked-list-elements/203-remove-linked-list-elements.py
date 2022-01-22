# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        if head.next is None and head.val == val:
            return None

        if head.next is None and head.val != val:
            return head

        prev = None
        curr = head
        while curr:
            if curr.val == val and prev is not None:
                prev.next = curr.next
                curr = curr.next
            elif curr.val == val and prev is None:
                head = curr.next
                prev = None
                curr = head

            else:
                prev = curr
                curr = curr.next

        return head
#         if not head:
#             return head
        
#         dummy, dummy.next = ListNode(0), head
        
#         pre, cur = dummy, head
#         while cur:
#             if cur.val == val:
#                 pre.next = cur.next
#             else:
#                 pre = cur                
#             cur = cur.next
            
#         return dummy.next