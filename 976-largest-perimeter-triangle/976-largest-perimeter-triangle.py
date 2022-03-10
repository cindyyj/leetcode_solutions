class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Without loss of generality, say the sidelengths of the triangle a≤b≤c.
        # The necessary and sufficient condition for these lengths to form a triangle of non-zero area is a + b > ca+b>c.
        
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
        