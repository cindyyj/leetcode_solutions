class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0 
        for s in sentences:
            most = max(most, len(s.split()))
        return most