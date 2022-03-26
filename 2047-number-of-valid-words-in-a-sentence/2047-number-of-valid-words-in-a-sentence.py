import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[,.!]?$')
        word_count = 0
        for word in sentence.split():
            if pattern.match(word):
                word_count += 1
                
        return word_count        