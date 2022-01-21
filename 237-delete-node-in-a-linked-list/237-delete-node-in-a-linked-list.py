# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
                
        goal : delete node 2.

        1  ->  2 -> 3       -> 4
           ^    ^
           |    |
          node  node.next
        #step one:  change the node value to 3
        1  ->  3   3           4
           ^    ^           ^
           |    |           |
          node  node.next   node.next.next

        #step two: change the next pointer to point to node.next.next
        1  ->  3   ->          4
           ^    ^           ^
           |    |           |
          node  node.next   node.next.next

        1 ->3 ->4
        
        Complexity Analysis

Time complexity: O(1)
The algorithm only needs two assignment operations.
Space complexity: O(1)
The algorithm doesn't need extra memory.
        """
        
        node.val = node.next.val
        node.next = node.next.next