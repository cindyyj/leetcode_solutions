class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
        
#         # Brute Force T: O(n2), S: O(1)
#         max_profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 max_profit = max(max_profit, prices[j] - prices[i])

#         return max_profit
        
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
            
            max_profit = max(max_profit, prices[i] - min_price)
                
        return max_profit