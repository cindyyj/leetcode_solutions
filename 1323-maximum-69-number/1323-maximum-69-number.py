class Solution:
    def maximum69Number (self, num: int) -> int:
        # string.replace(old, new, count)
        return int(str(num).replace("6", "9", 1))
            
        