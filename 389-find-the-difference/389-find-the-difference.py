class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # bit manipulation, 0 ^ x = x (xor)
        ch = 0 
        for c in s:
            ch ^= ord(c)
        for c in t:
            ch ^= ord(c)
        return chr(ch)
        
        
        
        # return (Counter(t) - Counter(s)).keys()
        
        # for char in t:
        #     if s.count(char) != t.count(char):
        #         return char