class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1, freq2 = Counter(words1), Counter(words2)
        return sum( freq1[w] == freq2[w] == 1 for w in freq1 )