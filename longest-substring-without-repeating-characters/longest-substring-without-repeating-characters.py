from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
        # hashmap 
        # time, O(n), space: O(min(m, n)), m is size of charset, n is len(s)
        
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