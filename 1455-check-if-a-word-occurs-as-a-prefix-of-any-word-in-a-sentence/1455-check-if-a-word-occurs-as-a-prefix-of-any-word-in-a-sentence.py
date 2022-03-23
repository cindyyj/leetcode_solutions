class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, w in enumerate(sentence.split()):
            # return the minimal index.
            if w.startswith(searchWord):
                return i + 1
        return -1