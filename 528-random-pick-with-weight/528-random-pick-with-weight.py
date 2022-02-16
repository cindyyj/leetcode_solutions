# class Solution:
#     def __init__(self, w):
#         self.w = w

#     def pickIndex(self):
#         # random.choices return a list!
#         return random.choices(range(len(self.w)), weights=self.w)[0]

import random
from itertools import accumulate

class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = self.pre[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)  # random.random() * self.total 
        
        l, r = 0, len(self.pre) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if self.pre[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return l
        
        # return bisect_left(self.pre, target)


# class Solution:
#     def __init__(self, w: List[int]):
#         """
#         :type w: List[int]
#         """
#         self.prefix_sums = []
#         prefix_sum = 0
#         for weight in w:
#             prefix_sum += weight
#             self.prefix_sums.append(prefix_sum)
#         self.total_sum = prefix_sum

#     def pickIndex(self) -> int:
#         """
#         :rtype: int
#         """
#         target = self.total_sum * random.random()
#         # run a linear search to find the target zone
#         for i, prefix_sum in enumerate(self.prefix_sums):
#             if target < prefix_sum:
#                 return i
        
"""
sampling with weight
sampling important step for building decision tree model 

- random.random(): Return random number between 0.0 and 1.0:
- random.choices(): returns a list with the randomly selected element from the specified sequence. Can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
- Random randint(start, stop): Return a integer between start and stop (both included)
- same as randrange(start, stop+1)

def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] <= x:    # <--- less than or equal to
            lo = mid+1
        else:
            hi = mid
    return lo


def bisect_left(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:    # <--- less than
            lo = mid + 1
        else:
            hi = mid
    return lo


pre[i]−w[i]+1≤x≤pre[i]

的 ii 并将其作为答案返回。由于 \textit{pre}[i]pre[i] 是单调递增的，因此我们可以使用二分查找在 O(\log n)O(logn) 的时间内快速找到 ii，即找出最小的满足 x \leq \textit{pre}[i]x≤pre[i] 的下标 ii。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/random-pick-with-weight/solution/an-quan-zhong-sui-ji-xuan-ze-by-leetcode-h13t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()