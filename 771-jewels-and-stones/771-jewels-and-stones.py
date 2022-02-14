class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # use hash set
        # Time Complexity: O(len(j) + len(s))
        # space: O(len(j)) or O(1)
        
        j = set(jewels)
        return sum(stone in j for stone in stones)
        
        # # brute force
        # # Time Complexity: O(len(j) * len(s))
        # # space: O(1)
        # return sum(stones.count(char) for char in jewels)