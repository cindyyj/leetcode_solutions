class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # bit manipulation
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        
#         # hashset
#         # time, O(n), traverse the list. Space: O(1)
        
#         for i in range(len(nums) + 1):
#             if i not in nums:
#                 return i 
        
#         # expected sum (n+1)*n/2 - actual sum
#         # 时间复杂度：O(n)，
#         # The time complexity of len() is O(1) , sum(list) O(n)
#         # The time complexity of Python sum() depends on your data structure. 
#         # For a flat list, dict you cannot do better than O(n) because you have to look at each item in the list to add them up.
#         # space: O(1)

#         return int((len(nums) + 1) * len(nums) / 2 - sum(nums))
