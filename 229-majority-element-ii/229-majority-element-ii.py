class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # set
        unique = set(nums)
        return [num for num in unique if nums.count(num) > len(nums) / 3]
        
        # Moore Voting
        
        
#         # HashMap
#         counts = collections.Counter(nums)
#         ans = []
        
#         for key, value in counts.items():
#             if value > len(nums)/3:
#                 ans.append(key)
                
#         return ans
        
#         # Brute Force: Time (O(n**2))
#         majority_count = len(nums) // 3
#         seen = []
#         ans = []
#         for num in nums:
#             if num not in seen:
#                 count = sum([1 for elem in nums if elem == num])
#                 if count > majority_count:
#                     ans.append(num)
#                     seen.append(num)
        
#         return ans