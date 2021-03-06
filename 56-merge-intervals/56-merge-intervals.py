class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/merge-intervals/solution/
        # https://leetcode.com/problems/merge-intervals/discuss/1644409/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Sort-Merge-O(NlogN)-%2B-Count-Sort-O(N-%2B-R)
        # official leetcode solution 
        # classic!!! 

# #  --------------------------- METHOD 1, sort, basic ---------------------------        
#         intervals.sort(key=lambda x : x[0])
#         merged = []
#         for i in intervals:
#             if not merged or i[0] > merged[-1][1]:
#                 merged.append(i)
#             else:
#                 merged[-1][1] = max(merged[-1][1], i[1])
#         return merged
        
# #  --------------------------- METHOD 2, in-place merge ---------------------------        

        intervals.sort(key=lambda x : x[0])
        # right end
        r = 0
        
        for i in intervals:
            if i[0] > intervals[r][1]:
                intervals[r := r + 1] = i
            else:
                intervals[r][1] = max(intervals[r][1], i[1])
        
        return intervals[:r+1]


"""
链接：https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
# if the list of merged intervals is empty or if the current
# interval does not overlap with the previous, simply append it.
# otherwise, there is overlap, so we merge the current and previous intervals.

Facebook Follow-Up
Question: How do you add intervals and merge them for a large stream of intervals? (Facebook Follow-up Question)

Inspired by https://leetcode.com/problems/merge-intervals/discuss/21452/Share-my-interval-tree-solution-no-sorting

We need to have two functions for the tree (add interval and query tree).

Implementation Details
TreeNode - On top of the left child, right child, start boundary, and end boundary, we have a middle field that determines whether a new interval goes to the left child, right right or merged with the current node.

add - If the new interval touches or crosses the middle of the current node, we update the current node. Otherwise, we put the new interval into the left subtree or right subtree.

Why do we use middle for comparison and not start or end boundaries?
The reason is that we can use merge-sort technique to query the merged intervals result when the left subtree does not overlap with the right subtree.
query - Use merge-sort technique by retrieving the merged intervals of the left subtree (i.e. left_intervals) and those of the right subtree (i.e. right_intervals). Because of the implementation of add, we can guarantee that

if there's an interval in the left_intervals that overlaps with the current node, then we know that all the intervals after that interval overlaps with the current node.
The first few intervals or zero intervals in the right_intervals overlap with the current node.
Here's the visualization:

left_res = [ (intervals that do not overlap), (intervals that overlap with current node) ]
right_res = [ (intervals that overlap with current node), (intervals that do not overlap) ]
Code
class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.root = None
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)
        
        return self.query(self.root)
    
    
    def add(self, node, start, end):     
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)
        
        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)
        
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)
    
    def query(self, node):
        if not node:
            return []
        
        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []
        
        inserted = False
        
        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
        
        if not inserted:
            res.append([node.start, node.end])
        
        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)
        
        return res

"""