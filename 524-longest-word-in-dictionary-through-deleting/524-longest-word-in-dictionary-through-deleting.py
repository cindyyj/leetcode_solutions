class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        # keeping the order after deleting some characters from given sting.
        dictionary.sort(key=lambda x:(-len(x), x))
        
        for word in dictionary:
            i, length = 0, len(word)
            for char in s:
                if word[i] == char: i += 1
                if i == length:
                    return word
        
        return ""
    
    
    """
    The built-in function iter() takes an iterable object and returns an iterator.
with state that remembers where it is during iteration,
c in it returns True if the value in the iteration and updates the state to point at the next value
return False when it goes to the end of iteration
just for those who are not familiar with iter() at first like me.

mistakes! 
# find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1. 
s.find(word): 

# # using Counter didn't preserve the order of characters!
# if not (Counter(word) - Counter(s)):
    """