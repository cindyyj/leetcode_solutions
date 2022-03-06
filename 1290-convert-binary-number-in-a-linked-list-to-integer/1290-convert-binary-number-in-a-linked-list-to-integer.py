# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            # num = num * 2 + head.next.val
            # better with bitwise operations
            num = (num << 1) | head.next.val
            
            head = head.next
        
        return num
        
#         # Use walrus operator in Python 3.8:
#         # https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/451815/JavaPython-3-Simulate-binary-operations.

#     def getDecimalValue(self, head: ListNode) -> int:
#         ans = head.val
#         while head := head.next:
#             ans = ans << 1 | head.val
#         return ans