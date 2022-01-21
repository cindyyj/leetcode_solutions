# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0      
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # invalid index
        if index < 0 or index >= self.size:
            return -1 
        
        # null linked list !!!
        if self.head is None:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        return self.addAtIndex(0, val)       

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked
        list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not
        be inserted.
        """
        
        # If index is greater than the length, the node will not be inserted.
        if index < 0 or index > self.size:
            return
        
        cur = self.head
        new_node = ListNode(val)
        
        # insert at head
        if index == 0:
            new_node.next = cur
            self.head = new_node
        
        # insert before index_th node
        else:
            for _ in range(index-1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        
        self.size += 1
      

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return 
        
        cur = self.head
        
        # if delete head node
        if index == 0:
            self.head = self.head.next
        else:
            # find prev node before index_th node
            for _ in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
            
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)