class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/1587270/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-%2B-Hashmap-%2B-XOR-%2B-Linear-%2B2-Binary-Search
        # binary search
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r-l) >> 1)
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]
            
        
        
        # # XOR
        # return reduce(xor, nums)
        
        # # set
        # return 2*sum(set(nums)) - sum(nums)
        
        # # Brute Force
        # for i in range(0, len(nums) - 2, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]