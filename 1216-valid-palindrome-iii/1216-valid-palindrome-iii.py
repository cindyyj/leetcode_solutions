class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Least Recently Used (LRU) strategy  
        # helps in reducing the execution time of the function by using memoization technique
        # @lru_cache(None) to implement memorization in python. 
        # None is the value for the input parameter maxsize of lru_cache. 
        # If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound.
  
        if s == s[::-1]:
            return True
        
        @lru_cache(None)
        def helper(lo, hi, k):
            while lo < hi:
                if s[lo] == s[hi]:
                    lo, hi = lo + 1, hi - 1
                elif k > 0:
                    return helper(lo, hi - 1, k - 1) or helper(lo + 1, hi, k - 1)
                else:
                    return False
            return True
        
        return helper(0, len(s) - 1, k)