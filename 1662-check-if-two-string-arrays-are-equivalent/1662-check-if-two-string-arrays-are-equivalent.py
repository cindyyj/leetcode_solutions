class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return ''.join(word1) == ''.join(word2)

    
    
class Solution:
    # Understanding generators and yield statement
    # https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/1007878/Python-Understanding-generators-and-yield-statement
    
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True
        # return all(c1 == c2 for c1, c2 in zip(self.gen(word1), self.gen(word2))

    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c
        # Ensure False when len(word1) != len(word2) 
        yield None