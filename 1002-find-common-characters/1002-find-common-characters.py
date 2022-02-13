from collections import Counter
from functools import reduce
from operator import and_

# nice example of reduce!!!
# class Solution:
#     def commonChars(self, A: List[str]) -> List[str]:
#         return list(reduce(and_, map(Counter, A)).elements())
    
    
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        cnt = Counter(words[0])
        for word in words[1:]:
            cnt &= Counter(word)
        return list(cnt.elements())
        