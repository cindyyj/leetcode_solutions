class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # 6. Boyer-Moore Voting. Time O(n), Space: O(1)
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        
        return candidate
        
        
#         # 5. Divide and Conquer
#         # 4. Random choice, O(inf)
#         # 3. Sort. Time O(nlogn), Space: O(1)
#         nums.sort() #list sort is in-place
#         return nums[len(nums) // 2]
        
#         # 2. HashMap: Time O(n), Space: O(n)
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)
        
#         # Brute Force: Time O(n**2), Space: O(1)
#         majority_count = len(nums) // 2
        
#         for num in nums:
#             count = sum([1 for elem in nums if num == elem])
#             if count > majority_count:
#                 return num     
        
#         # 6 solutions
#         # https://leetcode.com/problems/majority-element/solution/
        