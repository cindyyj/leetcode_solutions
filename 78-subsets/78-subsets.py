class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # https://leetcode.com/problems/subsets/solution/
        n = len(nums)
        
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
            
        return ans
        