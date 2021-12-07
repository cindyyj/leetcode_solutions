class Solution:
    def reverseWords(self, s: str) -> str:
        
# A.split() without arguments splits the string by " " (white space).
# string[::-1] slices the string backwards, we use it to get the reversed words.
# use list comprehension (x for x in list_of_x) to get the list of the reversed words.
# x.join(list) concatenates the elements in list together, with x in between as a separater.
          
        words = s.split()
        output = " ".join(word[::-1] for word in words)
        
        return output