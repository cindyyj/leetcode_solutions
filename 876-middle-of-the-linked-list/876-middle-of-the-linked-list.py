# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
#     作者：liweiwei1419
#     链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/kuai-man-zhi-zhen-zhu-yao-zai-yu-diao-shi-by-liwei/
#     来源：力扣（LeetCode）
#     著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
#     def create_linked_list(nums):
#         if len(nums) == 0:
#             return None
#         head = ListNode(nums[0])
#         cur = head
#         for i in range(1, len(nums)):
#             cur.next = ListNode(nums[i])
#             cur = cur.next
#         return head


#     def print_linked_list(list_node):
#         if list_node is None:
#             return

#         cur = list_node
#         while cur:
#             print(cur.val, '->', end=' ')
#             cur = cur.next
#         print('null')


#     if __name__ == '__main__':
#         # nums = [1, 2, 3, 4, 5, 6, 7]
#         nums = [1, 2, 3, 4, 5, 6, 7, 8]
#         head = create_linked_list(nums)
#         solution = Solution()
#         result = solution.middleNode(head)
#         print('Result：')
#         print_linked_list(result)