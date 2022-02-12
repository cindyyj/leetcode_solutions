class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 这题相比前面的题目加了一丢丢小的变通: 题目要求首尾串最大点数，其实就是求非首尾串的连续序列的最小点数
        # 特解
        
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        
        m = n - k
        total = 0
        minsum = float('inf')
        start = 0
        for end in range(n):
            total += cardPoints[end]
            
            if end >= m - 1:
                minsum = min(minsum, total)
                total -= cardPoints[start]
                start += 1

        return sum(cardPoints) - minsum
        
        # min score for continuous n - k array 
        # maximum score you can obtain