class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        s = [ s[i:i+k] for i in range(0, len(s), k)]
        
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
            
        return ''.join(s)
		# Divide s into an array of substrings length k
		# Reverse every other substring, beginning with s[0]
		# Join array of substrings into one string and return 
        
        
#         # https://leetcode.com/problems/reverse-string-ii/solution/
#         chars = list(s)
#         for i in range(0, len(chars), 2 * k):
#             chars[i:i+k] = reversed(chars[i:i+k])
        
#         return "".join(chars)

