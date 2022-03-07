class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build(s):
            ans = ""
            for c in s:
                if c != '#':
                    ans += c
                elif ans:
                    ans = ans[:-1]
            return ans
        
        return build(s) == build(t)                
                   
        