# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# # --------------------------- METHOD 1a ---------------------------
        # empty or one element
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
            # pre, cur, cur.next = cur, cur.next, pre
        return pre  
    
# # --------------------------- METHOD 1b ---------------------------    
#         # Iterative
        
#         pre, cur = None, head
        
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#             # this assignment is similar to python logic of swap variables
#             # x, y = y, x 
#             # x = tmp, x = y, y = tmp
#             # cur.next = tmp, cur.next = pre, pre = cur, cur = tmp            
        
#         return pre

# # --------------------------- METHOD 1c ---------------------------

#         #  Iterative Approach Easy Solution
#         # https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
#         # 记录当前节点的下一个节点
#         # 然后将当前节点指向pre
#         # pre和cur节点都前进一位
#         # end when cur is null (after the last node), thus return pre!
        
#         cur, pre = head, None
        
#         while cur:
            
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
            
#         return pre


# # --------------------------- METHOD 2 ---------------------------
        
#         # recursive
#         # 递归终止条件是当前为空，或者下一个节点为空
# 		# 这里的cur就是最后一个节点
# 		# 这里请配合动画演示理解
# 		# 如果链表是 1->2->3->4->5，那么此时的cur就是5
# 		# 而head是4，head的下一个是5，下下一个是空
# 		# 所以head.next.next 就是5->4
# 		# 防止链表循环，需要将head.next设置为空
# 		# 每层递归函数都返回cur，也就是最后一个节点
        
#         if head == None or head.next == None:
#             return head
#         cur = self.reverseList(head.next)
        
#         head.next.next = head
#         head.next = None
        
#         return cur
        


