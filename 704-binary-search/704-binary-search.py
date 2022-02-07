class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 
        
        
        # # 1-line
        # return nums.index(target) if target in nums else -1
        

# #         # https://leetcode.com/problems/binary-search/solution/
# #         Binary search is a textbook algorithm based on the idea to compare the target value to the middle element of the array.
# #         If the target value is equal to the middle element - we're done.
# #         If the target value is smaller - continue to search on the left.
# #         If the target value is larger - continue to search on the right.

# #         Algorithm
# #         Initialise left and right pointers : left = 0, right = n - 1.
# #             While left <= right :
# #                 Compare middle element of the array nums[pivot] to the target value target.
# #                 If the middle element is the target target = nums[pivot] : return pivot.
# #                 If the target is not yet found :
# #                 If target < nums[pivot], continue the search on the left right = pivot - 1.
# #                 Else continue the search on the right left = pivot + 1.

#         # binary search, Time: O(logN), Space: O(1)
        
#         l, r = 0, len(nums) - 1
        
#         while l <= r:
#             mid = l + (r-l) // 2
            
#             if nums[mid] < target:
#                 l = mid + 1
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 return mid
            
#         return -1 
        
#         # # nums.index() - O(n)
#         # if target in nums:
#         #     return nums.index(target)
#         # else: 
#         #     return -1
        