class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join([char for char in s.lower() if char.isalnum()])
        return sgood == sgood[::-1]
        