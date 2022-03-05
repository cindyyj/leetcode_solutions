class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = collections.Counter(s)
        nums = counts.values()
        
        odds = even = 0
        for num in nums:
            if num & 1:
                odds += 1
            else:
                even += 1
        
        return odds <= 1