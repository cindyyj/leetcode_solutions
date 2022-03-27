class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        # less than target, count of target
        lt, cnt = 0, 0
        for num in nums:
            if num < target:
                lt += 1
            elif num == target:
                cnt += 1
        return list(range(lt, lt + cnt))
        
        
        
#         # O(nlog(n))
#         nums.sort()
        
#         res = []
#         for i, num in enumerate(nums):
#             if num == target:
#                 res.append(i)
#         return res