class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # time: O(len(s))
        # space: O(len(s))
        
        cleaned_s = "".join([char for char in s.lower() if char.isalnum()])
        return cleaned_s == cleaned_s[::-1]
        