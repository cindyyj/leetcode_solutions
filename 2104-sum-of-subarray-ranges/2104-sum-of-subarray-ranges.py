class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # non-brute force solution not trivial!!!
        # brute force
        ans, n = 0, len(nums)
        for i in range(n):
            min_, max_ = nums[i], nums[i]
            for j in range(i, n):
                min_ = min(min_, nums[j])
                max_ = max(max_, nums[j])
                ans += max_ - min_
        return ans
        
