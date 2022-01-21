# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # two pointers, fast and slow pointers, still requires dummy
        
        dummy = ListNode(0, head)
        
        slow = fast = dummy
        
        for i in range(n):
            fast = fast.next
        
        # at last node 
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
        
        
# # --------------------------------------------        
#         # Stack (with dummy node)
# # 时间复杂度：O(L)，其中 L 是链表的长度。
# # 空间复杂度：O(L)，其中 L 是链表的长度。主要为栈的开销。
        
#         dummy = ListNode(0, head)
#         stack = list()
        
#         cur = dummy
#         # push all nodes in stack
#         while cur:            
#             stack.append(cur)
#             cur = cur.next
            
#         # pop n elements
#         for i in range(n):
#             stack.pop()
        
#         stack[-1].next = stack[-1].next.next
        
#         return dummy.next

# # --------------------------------------------
#     # 计算链表长度, 当遍历到第 L-n 个节点时, 它就是我们需要删除的节点。
# # 时间复杂度：O(L)，其中 L 是链表的长度。
# # 空间复杂度：O(1)。
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
            