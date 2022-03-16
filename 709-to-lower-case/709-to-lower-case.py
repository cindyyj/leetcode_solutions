class Solution:
    def toLowerCase(self, s: str) -> str:
        
        d = { chr(ord("A") + i) : chr(ord("a") + i) for i in range(26)}
        return "".join([d[c] if c in d else c for c in s])
        
        # return s.lower()