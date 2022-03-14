class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        key_rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res =[]
        for w in words:
            for row in key_rows:
                if set(w.lower()) <= row: # <= (issubset)
                    res.append(w)
        return res
    
    
"""
This is just me, but I tend to prefer "if x.issubset(y)" over "if x & y == y." 
First, the former reads "more naturally" to me and conveys the programmer's intentions more clearly. 
Second, when computing x & y, you're constructing a new and unnecessary data structure that probably requires linear time and space complexity to build. Third, I have a hunch that Python has some under-the-hood optimizations for comparing subsets, and those might get lost when you do an "==" comparison. Just my two cents.
"""
