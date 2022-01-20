class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
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