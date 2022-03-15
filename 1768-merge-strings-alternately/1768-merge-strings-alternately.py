class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        """
        index, out of bounds --> index error
        string/list slicing, out of bounds --> empty results
        
        The slicing operation doesn't raise an error if both your start and stop indices are larger than the sequence length. 
        This is in contrast to simple indexing—if you index an element that is out of bounds, Python will throw an index out of bounds error. 
        However, with slicing it simply returns an empty sequence.
        """
        
        n = min(len(word1), len(word2))
        res =""
        for i in range(n):
            res += word1[i] + word2[i]
        return res + word1[n:] + word2[n:]
        
        # return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
                
#         res = ""
#         l1, l2 = len(word1), len(word2)
#         minl = min(l1, l2)

#         for i in range(minl):
#             res += word1[i] + word2[i]
        
#         if l1 < l2:
#             res += word2[minl:]
#         elif l1 > l2:
#             res += word1[minl:]
#         return res