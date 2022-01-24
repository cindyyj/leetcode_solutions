# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # return mid point
    # Given the head of a singly linked list, return the middle node of the linked list.
    # If there are two middle nodes, return the first middle node.
    # to return second middle nodes, stop while fast and fast.next
# 时间复杂度：O（N）：N为链表长度
# 空间复杂度：O（1）：只修改链表的指向    

    def findMid(self, head):
        slow = fast = head        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next       
        return slow
    
    # reverse linked list given head
    def reverse(self, head):
        # empty or one element
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            # right version:
            # cur.next, pre, cur = pre, cur, cur.next
            
            # this is wrong
            # pre, cur, cur.next = cur, cur.next, pre
        return pre
    
    # note len(B) <= len(A), small in case of odd
    def comp_LL(self, headA, headB):
        while headB:
            if headA.val != headB.val:
                return False
            headA = headA.next
            headB = headB.next
        return True
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 找中点
        # 翻转一半
        # 比对
        # 还原（可有可无）
                
        # empty or one element
        if not head or not head.next:
            return True
        
        # at least two elements in LL
        # find mid
        A_end = self.findMid(head)
        B_start = A_end.next
        A_end.next = None
        
        # reverse
        B_start = self.reverse(B_start)
        
        # compare
        res = self.comp_LL(head, B_start)
        
        # # (optional) reverse
        # A_end.next = self.reverse(B_start)

        return res

    
        
# --------------------------- METHOD 2 ---------------------------

# # --------------------------- METHOD 1 ---------------------------
#         # idea: use list to store node vals
#         # Time: O(n), Space O(n)
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         vals = []
        
#         cur = head
#         # time O(n)
#         while cur:
#             vals.append(cur.val)
#             cur = cur.next
        
#         return vals == vals[::-1] # time O(n) for compare
        