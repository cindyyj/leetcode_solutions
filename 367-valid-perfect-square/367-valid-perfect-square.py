class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num <= 0: return False
        
        l, r = 1, num
        
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num < (mid + 1)*(mid + 1):
                return False
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        