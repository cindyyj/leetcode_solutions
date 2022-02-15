class Solution:
    def check(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/discuss/1053508/JavaC%2B%2BPython-Easy-and-Concise
        # Very clever to use the fact that nums[0] < nums[-1] is also considered in this
        return sum( nums[i - 1] > nums[i] for i in range(len(nums)) ) <= 1
        