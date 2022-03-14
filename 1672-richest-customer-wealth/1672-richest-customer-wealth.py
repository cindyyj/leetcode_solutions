class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [sum(row) for row in accounts]
        return max(wealth)        