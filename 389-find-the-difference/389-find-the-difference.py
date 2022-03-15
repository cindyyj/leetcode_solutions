class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        return list((Counter(t) - Counter(s)).keys())[0]
        
        # # bit manipulation, 0 ^ x = x (xor)
        # ch = 0 
        # for c in s:
        #     ch ^= ord(c) # ord is ASCII value, an integer representing the Unicode character.
        # for c in t:
        #     ch ^= ord(c)
        # return chr(ch) #chr = convert ASCII into character
        
        
        # for char in t:
        #     if s.count(char) != t.count(char):
        #         return char