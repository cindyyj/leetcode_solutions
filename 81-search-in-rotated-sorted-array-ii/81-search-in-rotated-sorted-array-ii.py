class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # search in roated sorted array, duplicate allowed
        # 如果第一个数和最后一个数不相等，那么跟上一题没有区别
        #如果第一个数和最后一个数相等，而且等于target，return true
        #如果第一个数和最后一个数相等，但是不等于target，在最坏的情况下就需要遍历两个升序数组的某一个，已确定target有可能落在哪一段，极端情况时间复杂度会降低到0(N)
        # https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/python-er-fen-cha-zhao-by-jiayangwu/

        # // 1. left to mid ordered and target is in [left, mid] 
        # // 2. Left to mid ordered but target in the other side [mid, right]
        # // 3. right to mid ordered, target in [mid, right]
        # // 4. right to mid ordered but in the other side in [left, mid]
        
        # null or empty array
        if not nums or not len(nums):
            return False
        
        if nums[0] == nums[-1] == target:
            return True
        
        l, r = 0, len(nums) - 1
        while l <= r:
            # to avoid duplicates
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            
            # same with Problem 33, find target in rotated array, no duplicate  
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1 
            
        return False
    

#         # https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/
#         return True if target in nums else False
        