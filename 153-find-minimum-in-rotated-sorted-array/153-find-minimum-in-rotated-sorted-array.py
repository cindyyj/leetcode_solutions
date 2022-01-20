class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
        # binary search
        # one-element or no rotation (last elem > 1st elem)
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while r >= l:
            mid = l + (r - l) // 2
            
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            # inflection point 
            
            # stop our search when we find the inflection point, when either of the two conditions is satisfied:
            # nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
            # nums[mid - 1] > nums[mid] Hence, mid is the smallest.

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # If mid element > first element of array this means that we need to look for the inflection point on the right of mid.
            # If mid element < first element of array this that we need to look for the inflection point on the left of mid.
            
            if nums[mid] > nums[0]:
                l = mid + 1
            if nums[mid] < nums[0]:
                r = mid - 1


#         # 1- liner, time: O(N)
#         # min, max have O(N) time complexity 
#         # because they have to loop over the given list/string and check every index to find min/max.

#         return min(nums)
        