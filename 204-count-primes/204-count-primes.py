class Solution:
    def countPrimes(self, n: int) -> int:
        
                ## APPROACH :  Sieve of Eratosthenes ##
        
        #   1. Checking till sqrt(n) is enough for prime numbers i.e i*i < n
        #   2. mark all as prime.
        #   3. as you move along (i to i*i<n) mark every multiple until n as False.
        #   4. you donot need start from i for that we can start from i*i i.e j=i*i
        
		## TIME COMPLEXITY : O(NLogN) ##
		## SPACE COMPLEXITY : O(N) ##
        # Loop's ending condition is i * i < n instead of i < sqrt(n) to avoid repeatedly calling an expensive function sqrt().
        
        if n <= 2: return 0
        
        dp = [1] * n
        dp[0] = dp[1] = 0
        
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = 0
        return sum(dp)