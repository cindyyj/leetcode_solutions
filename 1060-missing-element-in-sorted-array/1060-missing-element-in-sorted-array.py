class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:


        len_n = len(nums)
        missing = nums[-1] - nums[0] + 1 - len_n
        if k > missing:
            return nums[-1] + k - missing
        
        # Now the first missing number must be inside nums.
        last, left, right = 0, 0, len_n-1
        while left <= right:
            mid = left + (right - left) // 2
            missing = nums[mid] - nums[last] + 1 - (mid-last+1)
            if k > missing:
                last = mid
                k -= missing
                left = mid + 1
            else:
                right = mid - 1
        return nums[last] + k        
    
    '''
    The idea is to find the leftmost element such that the number of missing numbers until this element is smaller or equal to k.
    
Binary search
calculate number_range = nums[-1] - nums[0] + 1
The count of missing numbers, missing = number_range - len(nums)
if k > missing, the wanted missing number is not inside the number list. result = nums[-1] + k - missing.

We can apply Binary search to solve this problem.
if missing number is not inside nums[left:mid+1], search in nums[mid+1:right+1] and update k -= missing.
Otherwise search in nums[left:mid-1].
Use the 'last' variable to track the starting of the region with missing number.
Time: O(logn)
Space: O(1)
    '''