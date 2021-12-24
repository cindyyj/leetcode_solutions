class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]