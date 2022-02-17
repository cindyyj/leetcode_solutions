class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char : i for i, char in enumerate(order)}        
        words = [[d[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))