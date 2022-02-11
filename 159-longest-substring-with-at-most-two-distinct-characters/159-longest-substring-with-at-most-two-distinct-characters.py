from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
# 作者：eason734
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
        n = len(s)
        if n <= 2:
            return n
        
        maxlen = 2
        hashmap = defaultdict(int)
        
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] += 1
            
            while len(hashmap) > 2:
                hashmap[s[start]] -= 1
                
                # del dictionary["key"], Remove Key from a Dictionary Python: del
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                
                start += 1
                
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen             
