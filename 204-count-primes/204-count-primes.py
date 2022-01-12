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
        # All the for construct does is loop over an iterable. If that iterable is empty, then the body of the for is never executed.

        # All range does is return an interable containing all the values from start to stop (inclusive of start, exclusive of stop). If start is higher than stop, then the iterable is empty because there are no valid values between start and stop:

        # >>> range(0, 2):
        # [0, 1]
        # >>> range(2, 0):
        # []
        # Putting this together means that you now have a for loop with an empty iterable - so it doesn't get iterated over at all.        
        
        if n <= 2: return 0
        
        dp = [1] * n
        dp[0] = dp[1] = 0
        
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = 0
        return sum(dp)