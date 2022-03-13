class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        Actually, your rule could be derived from constructing an arithmetic sequence.
        NOTE: Any arithmetic sequence must have unique values if the common delta is non-zero.
        We need the sequence sum, i.e., (a[0] + a[n-1])*n / 2, to be 0, which means a[0] + a[n-1] = 0.
        Note that a[n-1] - a[0] = (n-1)*delta, which is -2*a[0], so we simply set
        delta = 2, a[0] = 1-n;
        """
        return [x for x in range(1-n, n, 2)]
        
        
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
        