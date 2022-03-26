class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        # same as 616: https://leetcode.com/problems/add-bold-tag-in-string/
        
        n = len(s)
        bold = [False] * n
        
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)
        
        ans = ""
        i = 0
        while i < n:
            if bold[i]:
                ans += "<b>"
                while i < n and bold[i]:
                    ans += s[i]
                    i += 1
                ans += "</b>"
            else:
                ans += s[i]
                i += 1
            
        return ans