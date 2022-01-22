# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        
        return A     
        
#         考虑构建两个节点指针 A , B 分别指向两链表头节点 headA , headB ，做如下操作：

#         指针 A 先遍历完链表 headA ，再开始遍历链表 headB ，当走到 node 时，共走步数为：
#         a + (b - c)
#         a+(b−c)

#         指针 B 先遍历完链表 headB ，再开始遍历链表 headA ，当走到 node 时，共走步数为：
#         b + (a - c)
#         b+(a−c)

#         如下式所示，此时指针 A , B 重合，并有两种情况：

#         a + (b - c) = b + (a - c)
#         a+(b−c)=b+(a−c)

#         若两链表 有 公共尾部 (即 c > 0c>0 ) ：指针 A , B 同时指向「第一个公共节点」node 。
#         若两链表 无 公共尾部 (即 c = 0c=0 ) ：指针 A , B 同时指向 nullnull 。

#         作者：jyd
#         链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
#         来源：力扣（LeetCode）
#         著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。