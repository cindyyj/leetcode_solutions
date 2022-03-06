BASE = 7

class Solution:
    def convertToBase7(self, num: int) -> str:

        # https://leetcode-cn.com/problems/base-7/solution/pythonjavajavascriptgo-zhan-zhuan-xiang-752fe/
        
        if num == 0:
            return str(num)
        
        neg = num < 0
        num = abs(num)
        
        ans = []
        while num > 0:
            ans.append(str(num % 7))
            num //= 7
        
        return ("-" if neg else "") + "".join(ans[::-1])