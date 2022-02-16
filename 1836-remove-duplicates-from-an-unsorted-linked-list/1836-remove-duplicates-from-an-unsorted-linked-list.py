# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        d = defaultdict(int)
        cur = head
        while cur:
            d[cur.val] += 1
            cur = cur.next
            
        dummy = ListNode(0)
        dummy.next = head
        
        pre, cur = dummy, head
        while cur:
            if d[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        
        return dummy.next