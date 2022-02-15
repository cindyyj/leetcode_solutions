class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        n = len(sentence)
        if n < 26:
            return False
        
        return len(Counter(sentence)) == 26
        
        