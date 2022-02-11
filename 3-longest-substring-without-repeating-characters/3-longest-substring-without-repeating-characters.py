from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxlen = 0
        hashmap = Counter()
        
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] += 1
            
            while hashmap[s[end]] > 1:
                hashmap[s[start]] -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            
        return maxlen