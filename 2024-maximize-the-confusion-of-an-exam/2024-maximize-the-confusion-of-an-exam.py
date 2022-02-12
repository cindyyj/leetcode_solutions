from collections import defaultdict

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Intuition Open lee215's old post in 424. Longest Repeating Character Replacement,

        maxlen = maxf = 0
        d = defaultdict(int)
        
        start = 0
        for end, char in enumerate(answerKey):
            d[char] += 1
            maxf = max(maxf, d[char])
            
            if (end - start + 1) - maxf <= k:
                maxlen = max(maxlen, (end - start + 1))
            else: # >k
                d[answerKey[start]] -= 1
                start += 1
        
        return maxlen