class Solution:
    
    def getNext(self, n):        
        return sum([d ** 2 for d in list(map(int, str(n)))])        
        
#         happy_sum = 0
        
#         while n:            
#             # n, digit = (n // 10, n % 10) = divmod(n, 10)            
#             happy_sum += (n % 10) ** 2
#             n //= 10
            
#         return happy_sum
    
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNext(n)
            
        return n == 1
            
        # 将当前数替换为它每个位置上的数字的平方和。
        # 如果为1，则是快乐数
        # 如果替换后的数再之前出现过，则说明陷入无限循环，此数不是快乐数

        # https://leetcode.com/problems/happy-number/solution/
        # Determining the time complexity for this problem is challenging for an "easy" level question. If you're new to these problems, have a go at calculating the time complexity for just the getNext(n) function (don't worry about how many numbers will be in the chain).
        # very hard to determine time complexity!!!     