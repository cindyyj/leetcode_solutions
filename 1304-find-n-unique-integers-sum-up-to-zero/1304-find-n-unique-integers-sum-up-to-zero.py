class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        return range(1 - n, n, 2)
        # return [x for x in range(1-n, n, 2)]
        
        
        # ans = [num for num in range(1, n)]
        # ans.append(- sum(ans))
        # return ans        
        
        
        # res =[]
        # for i in range(1, n // 2 + 1):
        #     res.append(i)
        #     res.append(-i)            
        # if n & 1: # n % 2 == 1
        #     res.append(0)        
        # return res
        