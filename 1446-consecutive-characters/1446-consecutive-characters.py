class Solution:
    def maxPower(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        l = maxlen = 1
        prev = s[0]
        for char in s[1:]:
            if char == prev:
                l += 1
                maxlen = max(maxlen, l)
            else:
                l = 1
                prev = char
        return maxlen            