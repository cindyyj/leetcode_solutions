from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Sliding Window + Hashmap.
        maxlen = k
        n = len(s)
        
        if n <= k:
            return n
        
        start = 0
        hashmap = defaultdict(int)
        for end in range(n):
            hashmap[s[end]] += 1
            
            while len(hashmap) > k:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]] 
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            
        return maxlen