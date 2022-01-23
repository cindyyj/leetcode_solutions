# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Test case	Explanation
        # l1=[0,1]. l2=[0,1,2]	When one list is longer than the other.
        # l1=[], l2=[0,1]	When one list is null, which means an empty list.
        # l1=[9,9], l2=[1]	The sum could have an extra carry of one at the end, which is easy to forget.
        
        dummy = ListNode(0)
        cur = dummy
        carry = 0
            
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
            carry, digit = divmod(val1+val2+carry, 10)
            
            cur.next = ListNode(digit)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        