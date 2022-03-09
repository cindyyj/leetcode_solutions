class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        nums = "".join([str(ord(ch) - ord('a') + 1) for ch in s])
        while k:
            nums = str(sum(list(map(int, nums))))            
            k -= 1
        
        return int(nums)            