# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # https://leetcode.com/problems/first-bad-version/solution/
        
        # Initial Condition: left = 0, right = length-1
        # Termination: left > right
        # Searching Left: right = mid-1
        # Searching Right: left = mid+1
        
        l, r = 1, n
        
        while l <= r:
            mid = l + (r-l) // 2
            
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid 
            
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1