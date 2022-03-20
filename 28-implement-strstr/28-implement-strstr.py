class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # KMP for string pattern searching
        if not needle:
            return 0
        return haystack.find(needle)