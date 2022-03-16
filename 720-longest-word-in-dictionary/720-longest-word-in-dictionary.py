class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda word : (-len(word), word))
        
        for word in words:
            if all(word[:k] in words for k in range(1, len(word))):
                return word
        
        return ""