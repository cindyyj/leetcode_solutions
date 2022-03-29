class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        return sum(1 for num in nums if min_ < num < max_)