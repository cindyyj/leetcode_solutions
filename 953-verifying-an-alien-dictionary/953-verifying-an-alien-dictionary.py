class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # create mapping to a-z
        d = {char : chr(ord('a') + i) for i, char in enumerate(order)}
        for i in range(len(words)):
            words[i] = ''.join([d[c] for c in words[i]])        
        return sorted(words) == words
        
        # outtab = "abcdefghijklmnopqrstuvwxyz"
        # trantab = "".maketrans(order, outtab) # "".maketrans(order, string.ascii_lowercase)
        # for i in range(len(words)):
        #     words[i] = words[i].translate(trantab)
        # return words == sorted(words)
        
#         d = {char : i for i, char in enumerate(order)}
        
#         for i in range(len(words) - 1):
#             word1 = [d[c] for c in words[i]] 
#             word2 = [d[c] for c in words[i + 1]]
            
#             for j in range(len(word1)):
#                 if j >= len(word2):  # "app" < "apple"
#                     return False
                
#                 if word1[j] != word2[j]:
#                     if word1[j] > word2[j]:
#                         return False
#                     else:  
#                         # if we find the first different character and they are sorted,
#                         # then there's no need to check remaining letters
#                         break
        
#         return True
            
        
        
        # # lee215
        # d = {char : i for i, char in enumerate(order)}        
        # words = [[d[c] for c in w] for w in words]
        # return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
    
        # # one-line 
        # # https://leetcode-cn.com/problems/verifying-an-alien-dictionary/solution/python-yi-xing-by-wang-hao-bi0glutbvu/
        # return words == sorted(words,key=lambda s:''.join(['abcdefghijklmnopqrstuvwxyz'[order.index(i)] for i in s]))

