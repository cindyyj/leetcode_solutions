class Solution:
    def capitalizeTitle(self, title: str) -> str:
    
        capitalized = []
        words = title.split()
        
        for w in words:
            if len(w) >= 3:
                capitalized.append(w.capitalize())
            else:
                capitalized.append(w.lower())
        
        return " ".join(capitalized)