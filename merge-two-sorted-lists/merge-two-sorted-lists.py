# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
        
        
#         # dummy head node
#         # Iterative, Time O(m+n), Space: O(1)
        
#         dummy = cur = ListNode(0)
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 cur.next = list1
#                 list1 = list1.next
#             else:
#                 cur.next = list2
#                 list2 = list2.next
#             cur = cur.next
            
#         cur.next = list1 if list1 else list2
        
#         return dummy.next             
        
        