class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # # XOR
        # return reduce(xor, nums)
        
        # set
        return 2*sum(set(nums)) - sum(nums)
        
        # # Brute Force
        # for i in range(0, len(nums) - 2, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]