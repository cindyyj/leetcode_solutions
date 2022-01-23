class Solution:
    
    def _isPalindrome(self, s):
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        
        # two pointer
        # 时间复杂度：O(n)，其中 n 是字符串的长度。
        # 判断整个字符串是否是回文字符串的时间复杂度是 O(n)，遇到不同字符时，判断两个子串是否是回文字符串的时间复杂度也都是 O(n)。
        # 空间复杂度：O(1)。只需要维护有限的常量空间。

        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                delete_l = s[l+1:r+1]
                delete_r = s[l:r]
                return self._isPalindrome(delete_l) or self._isPalindrome(delete_r)
            l += 1
            r -= 1
        
        return True