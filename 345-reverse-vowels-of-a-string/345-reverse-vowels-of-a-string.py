class Solution:
    def isVowel(self, ch: str) -> bool:
        return ch in 'aeiouAEIOU'
    
    def reverseVowels(self, s: str) -> str:
        
        n = len(s)
        s = list(s)
        l, r = 0, n - 1
        while l < r:
            while l < r and not self.isVowel(s[l]):
                l += 1
            while l < r and not self.isVowel(s[r]):
                r -= 1
                
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return "".join(s)


# 链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/fan-zhuan-zi-fu-chuan-zhong-de-yuan-yin-2bmos/
