class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words
        """
        Time complexity : O(n^3) There are two nested loops, and substring computation at each iteration. Overall that results in O(n^3) time complexity.
        Space complexity : O(n). Length of p array is n+1.
        """
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]        