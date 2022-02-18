class Solution:
#     def getColWord(self,i,words):
#         temp = ""
#         for word in words:
#             if i < len(word): temp+=word[i]
#         return temp
        
#     def validWordSquare(self, words):
#         """
#         :type words: List[str]
#         :rtype: bool
#         """      
#         for i,rowWord in enumerate(words):
#             colWord = self.getColWord(i,words)
#             if colWord != rowWord:
#                 return False
#         return True
    
    
    def validWordSquare(self, words):
        try:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except IndexError:
            return False