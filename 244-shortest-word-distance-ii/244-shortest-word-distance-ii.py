class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.d[word].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        p1, p2 = self.d[word1], self.d[word2]
        i = j = 0
        res = abs(p2[0]-p1[0])
        
        while i < len(p1) and j < len(p2):
            res = min(res, abs(p1[i] - p2[j]))
            if p1[i] < p2[j]:
                i += 1
            else:
                j += 1
        
        return res
        
   

    """
    time complexity:

    for constructor is O(n). n is the length of words list
    for shortest() is O(k), k is the total frequency of word1 and word2

    spacy complexity:

    for constructor is O(n)
    for shortest is O(1)
    """

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)