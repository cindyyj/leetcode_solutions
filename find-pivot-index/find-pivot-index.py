class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time Complexity: O(N), where NN is the length of nums.
        # Space Complexity: O(1), the space used by leftsum and S.        
        s= sum(nums)
        
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == s - left_sum - num:
                return i
            left_sum += num
        
        return -1