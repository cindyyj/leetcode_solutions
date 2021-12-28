class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
#         # Math solution: sum of 1 to n, len(nums) is n+1! n = (len(nums)-1)
#         # O(1); repeated number can appear more than 1 time!!! so this doesn't work!
#         series_sum = len(nums)*(len(nums)-1)/2
#         nums_sum = sum(nums)
        
#         return int(nums_sum-series_sum)
        
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        # 7 methods!!!
        
        # Time complexity: O(n**2): nested loop
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        
        # Time complexity: O(n), one loop; space: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
