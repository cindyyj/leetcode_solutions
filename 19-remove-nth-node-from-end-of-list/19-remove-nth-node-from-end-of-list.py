# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Stack (with dummy node)
        
        dummy = ListNode(0, head)
        stack = list()
        
        cur = dummy
        # push all nodes in stack
        while cur:
            stack.append(cur)
            cur = cur.next
            
        # pop n elements
        for i in range(n):
            stack.pop()
        
        stack[-1].next = stack[-1].next.next
        
        return dummy.next
    
#     # 计算链表长度, 当遍历到第 L-n 个节点时, 它就是我们需要删除的节点。
#     def get_length(self, head):
#         length = 0
#         while head:
#             length += 1
#             head = head.next
#         return length
        
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         # in case deleted head node ! use a dummy node
#         dummy = ListNode(0, head)
#         cur = dummy        
#         for i in range(self.get_length(head) - n):
#             cur = cur.next        
#         cur.next = cur.next.next
        
#         return dummy.next
            