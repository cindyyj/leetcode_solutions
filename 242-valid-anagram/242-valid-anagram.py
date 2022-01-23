class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # https://leetcode-cn.com/problems/valid-anagram/solution/pai-xu-bi-dui-ha-xi-ji-lu-ci-shu-by-cht_-4vex/
        
        if len(s) != len(t):
            return False
        
        count = [0]*26 # count of appearance of a to z, 'a' = chr(ord('a'))
        
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
        
        for i in range(len(t)):
            count[ord(t[i])-ord('a')] -= 1
        
        return count == [0]*26

#         # one-line
#         if len(s) != len(t):
#             return False
        
#         return collections.Counter(s) == collections.Counter(t)