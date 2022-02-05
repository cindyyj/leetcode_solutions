class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        # good review on string operations! 
        
        words = text.split() # split(sep=None) will discard empty strings.
        
        # word count
        cnt = len(words)
        
        # space count
        spaces = text.count(' ')
        
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
      # trailing_spaces = spaces if gap == 0 else spaces % (cnt - 1)
        trailing_spaces = spaces - gap * (cnt - 1) # credit to @madno
        
        return (' ' * gap).join(words) + ' ' * trailing_spaces                