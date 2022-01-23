class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # two pointer
        
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].lower().isalnum():
                l += 1
            elif not s[r].lower().isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True
            
        
        
#         # time: O(len(s))
#         # space: O(len(s))
        
#         cleaned_s = "".join([char for char in s.lower() if char.isalnum()])
#         return cleaned_s == cleaned_s[::-1]
        