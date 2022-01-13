class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # Brute Force:
        majority_count = len(nums) // 3
        seen = []
        ans = []
        for num in nums:
            if num not in seen:
                count = sum([1 for elem in nums if elem == num])
                if count > majority_count:
                    ans.append(num)
                    seen.append(num)
        
        return ans
#         majority_count = len(nums) // 2
        
#         for num in nums:
#             count = sum([1 for elem in nums if num == elem])
#             if count > majority_count:
#                 return num             