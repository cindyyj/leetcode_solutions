class Solution:
    def maxDepth(self, s: str) -> int:
        # Amazon phone interview!
        
        # Ignore digits and signs,
        # only count the current open parentheses cur.
        # The depth equals to the maximum open parentheses.
        # Complexity
        # Time O(N)
        # Space O(1)
        # can simplify as it's known to be valid parentheses strings
        
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            if c == ')':
                cur -= 1
        return res        