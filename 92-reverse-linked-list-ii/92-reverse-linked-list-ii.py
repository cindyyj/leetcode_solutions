# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # https://leetcode.com/problems/reverse-linked-list-ii/solution/
        
        # Recursion
        # Time Complexity: O(N) since we process all the nodes at-most twice. 
        # Once during the normal recursion process and once during the backtracking process. 
        # During the backtracking process we only just swap half of the list if you think about it, but the overall complexity is O(N).
        # Space Complexity: O(N) in the worst case when we have to reverse the entire list. This is the space occupied by the recursion stack.
        
        # Iterative
        # Time Complexity: O(N) considering the list consists of N nodes. 
        # We process each of the nodes at most once (we don't process the nodes after the n-th node from the beginning.
        # Space Complexity: O(1) since we simply adjust some pointers in the original linked list and only use O(1) additional memory for achieving the final result.
        
        # Empty list
        if not head:
            return None
        
        # left <= right        
        if left == right:
            return head
        
        # 1-indexed 
        # using the dummy pattern because 
        # left can be 1 i.e. we may need to
        # reverse the list from the beginning too
        dummy = pre = ListNode(0)
        dummy.next = head
        cur = head
                
        # keep track of left - 1 (the node before left, left can be 1st node)
        for _ in range(left - 1):
            pre = cur
            cur = cur.next
            
        pre_start, start = pre, cur  # save left-1, left
        
        # reverse the nodes from left..right      
        for _ in range(right - left):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        # adjust final connections
        pre_start.next = cur
        start.next = cur.next
        cur.next = pre
        
        return dummy.next
            
        
            