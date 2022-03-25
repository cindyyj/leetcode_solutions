class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        
        res = []
        for word in sentence.split():
            found = False
            for i in range(1, len(word) + 1):
                if word[:i] in roots:
                    res.append(word[:i])
                    found = True
                    break
            
            if not found:
                res.append(word)
                
        return " ".join(res)