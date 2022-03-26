"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
    # 我们可以将题目说的多级双向链表看作是一棵二叉树，其中链表的child对应二叉树的left，链表的next对应二叉树的right，
    # 这样我们就可以将链表的扁平化看作二叉树的先序遍历。所以，我们可以采用深搜的方式解决这道题。

    # 作者：BNDSllx
    # 链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/solution/suan-fa-xiao-ai-lian-biao-ye-you-xian-xu-otl2/
    
        def dfs(node: "Node") -> "Node":
            cur = node
            # 记录链表的最后一个节点
            last = None

            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    child_last = dfs(cur.child)
                    
                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head