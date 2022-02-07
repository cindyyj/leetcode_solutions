class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # sliding window, time O(n)
        
        if not nums:
            return 0
        
        n = len(nums)
        start = end = 0 #window start end
        total = 0
        ans = n+1
        
        for end in range(n):
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
        return 0 if ans == n+1 else ans
        
        
#         # brute force, time exceeds. Time O(n2), Space O(1)
#         if not nums:
#             return 0
        
#         n = len(nums)
#         ans = n+1
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[j]
#                 if total >= target:
#                     ans = min(ans, j-i+1)
#                     break
        
#         return 0 if ans == n+1 else ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        