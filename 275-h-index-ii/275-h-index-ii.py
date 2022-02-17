class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < c for i, c in enumerate(citations[::-1]))