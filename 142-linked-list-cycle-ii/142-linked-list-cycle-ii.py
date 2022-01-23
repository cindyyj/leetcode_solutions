# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # trick: fast, slow meet twice
        
        if not head or not head.next:
            return None
        
        slow = fast = pointer = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        
        if not fast or not fast.next:
            return None
        
        while slow != pointer:
            slow = slow.next
            pointer = pointer.next
        
        return slow          
        
#         Proof:
#         If no cycle exists , fast pointer will reach the end and we will detect no cycle.
#         If there is a cycle , then both fast and slow pointer will enter into the cycle. We know that in every step fast jumps twice and slow jumps once which means that the distance between them increases by 1 in every step. This increment will keep happening and the pointers meet when the difference becomes a multiple of cycle length.

#         Detecting the entry point of cycle:
#         Algo: If we move a pointer from head of list and another from where the two pointers met in the cycle, then their meeting point is the entry point
#         Proof:
#         let the fast and slow pointers meet at distance a from the head of list.

#         Which means slow pointer travelled distance a and fast therefore travelled 2*a
#         Difference = 2a-a = a = multiple of k (k=chain length)
#         let the distance of head from entry point be m then distance of meeting point from entry point = a-m
#         The distance of meeting point from entry point from other side of cycle is k - (a-m) i.e k-a+m
#         This distance is (multiple)k + m = m therefore the distance from head to entry point = entry point from meeting point
#         Check diagram for better understanding.
        