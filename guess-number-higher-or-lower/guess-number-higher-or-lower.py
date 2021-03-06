# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # https://leetcode.com/problems/guess-number-higher-or-lower/solution/
        # Ternary Search example
        # binary search, Time complexity : O(log2n), S: O(1)
        if n == 1:
            return 1
        
        l, r = 1, n
        
        while l <= r:
            mid = l + (r-l) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
        
        return -1         