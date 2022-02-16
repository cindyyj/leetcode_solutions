class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        p1, p2 = wordsDict.index(word1), wordsDict.index(word2)        
        d = abs(p1 - p2)
        
        for i, word in enumerate(wordsDict):
            if word ==word1:
                p1 = i 
                d = min(abs(i-p2), d)
            elif word == word2:
                p2 = i
                d = min(abs(p1-i), d)
            
        return d