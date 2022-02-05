class Solution:
    def arrangeWords(self, text: str) -> str:
        # one-line string operations  &  sorted !!! 
        # classic
        return (" ").join(sorted(text.split(), key=len)).capitalize()        