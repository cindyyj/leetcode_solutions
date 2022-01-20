class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

# Basic Idea: Binary search

# Elaboration: 
#  if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either 
#    1. always increasing  -> the right-most element is the peak
#    2. always decreasing  -> the left-most element is the peak
#    3. first increasing then decreasing -> the pivot point is the peak
#    4. first decreasing then increasing -> the left-most element is the peak  

#    Therefore, we can find the peak only on its right elements( cut the array to half)

#    The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.



# Conditions:
#      1. array length is 1  -> return the only index 
#      2. array length is 2  -> return the bigger number's index 
#      3. array length is bigger than 2 -> 
#            (1) find mid, compare it with its left and right neighbors  
#            (2) return mid if nums[mid] greater than both neighbors
#            (3) take the right half array if nums[mid] smaller than right neighbor
#            (4) otherwise, take the left half

# Run time: O(logn)
# Memory: constant
# Test cases: 
#      [1]
#      [1,2]
#      [2,1]
#      [1,2,3]
#      [3,2,1]
#      [2,1,3]
        
        # binary search, Time complexity : O(log_2(n))
        # We reduce the search space in half at every step. Thus, the total search space will be consumed in log_2(n)
        
        # numbers descending order, down
        # numbers ascending order,  up
        # numbers can go up and down
        
        #  MIT 6006's 1st lecture on 'Algorithmic thinking and Peak Finding'
        # (timestamp for divide and conquer strategy for peak finding : 27.40 min). 
        # You will understand the correctness of the algorithm(binary search in peak finding). 
        # Lecturer also showed the master theorem for this also.Never miss the 2D version of peak finding in the lecture.
        # https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2&t=0s
        
        if not nums:
            return -1 
        
        if len(nums) == 1:
            return 0
        
        # 先特判两边情况
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1
        
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            mid = l + (r-l) // 2
            
            # 当前为峰值
            if (mid-1>=0 and mid+1 <=len(nums)-1) and ((nums[mid-1] < nums[mid]) and (nums[mid+1] < nums[mid])):
                return mid
            
            #  峰值在 mid 左侧
            if mid-1>=0 and nums[mid-1] > nums[mid]:
                r = mid - 1
            
            # 峰值在 mid 右侧
            else:
                l = mid + 1
        
        return -1 
    
        # # find max
        # return nums.index(max(nums))