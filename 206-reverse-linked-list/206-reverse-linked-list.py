# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #  Iterative Approach Easy Solution
        # https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
        # 记录当前节点的下一个节点
        # 然后将当前节点指向pre
        # pre和cur节点都前进一位
        # end when cur is null (after the last node), thus return pre!
        
        cur, pre = head, None
        
        while cur:
            
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        return pre
        