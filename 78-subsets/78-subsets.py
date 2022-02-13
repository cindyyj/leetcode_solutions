class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]])
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)
        
        
        
#         # https://leetcode.com/problems/subsets/solution/
#         n = len(nums)
        
#         ans = [[]]
#         for num in nums:
#             ans += [curr + [num] for curr in ans]
            
#         return ans
        