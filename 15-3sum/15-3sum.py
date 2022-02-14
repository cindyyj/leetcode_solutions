class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        res = []
        nums.sort()      
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, res)
        
        return res
    
    # def twoSum(self, nums, i, res):        
    #     l, r = i + 1, len(nums) - 1
    #     while l < r:
    #         total = nums[i] + nums[l] + nums[r]
    #         if total < 0:
    #             l += 1
    #         elif total > 0:
    #             r -= 1
    #         else:
    #             res.append([nums[i], nums[l], nums[r]])
    #             l += 1
    #             r -= 1
    #             while l < r and nums[l] == nums[l - 1]:
    #                 l += 1
        
    
    def twoSum(self, nums, i, res):                 
        seen = set()        
        j = i + 1
        while j < len(nums):
            complement = - nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


    

        
        
        
"""
1. For the main function:

Sort the input array nums.
Iterate through the array:
    If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
    If the current value is the same as the one before, skip it.
    Otherwise, call twoSumII for the current position i.
    
2. For twoSumII function:

Set the low pointer lo to i + 1, and high pointer hi to the last index.
While low pointer is smaller than high:
    If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
    If sum is greater than zero, decrement hi.
    Otherwise, we found a triplet:
        Add it to the result res.
        Decrement hi and increment lo.
        Increment lo while the next value is the same as before to avoid duplicates in the result
"""

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:    
#         # super long optimized solutions
#         # https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
#         if len(nums) < 3:
#             return []

#         res = set()

#         # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
#         n, p, z = [], [], []
#         for num in nums:
#             if num > 0:
#                 p.append(num)
#             elif num < 0:
#                 n.append(num)
#             else:
#                 z.append(num)

#         # 2. Create a separate set for negatives and positives for O(1) look-up times
#         N, P = set(n), set(p)

#         # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
#         #   i.e. (-3, 0, 3) = 0
#         if z:
#             for num in P:
#                 if -1 * num in N:
#                     res.add((-1 * num, 0, num))

#             # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
#             if len(z) >= 3:
#                 res.add((0, 0, 0))

#         # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
#         #   exists in the positive number set
#         from itertools import combinations

#         for x, y in combinations(n, 2):
#             target = -1 * (x + y)
#             if target in P:
#                 res.add(tuple(sorted([x, y, target])))

#         # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
#         #   exists in the negative number set

#         for x, y in combinations(p, 2):
#             target = -1 * (x + y)
#             if target in N:
#                 res.add(tuple(sorted([x, y, target])))

#         return [list(x) for x in res]