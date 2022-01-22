# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 基本思路设计两个指针，fast一次走两步，slow一次走一步。当fast或fast->next为空时，slow必定指向中间节点
        
        if not head or not head.next:
            return None
        
        dummy, dummy.next = ListNode(0), head
        pre, slow, fast = dummy, head, head
        
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        
        pre.next = slow.next
        
        return head        