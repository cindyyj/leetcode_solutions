class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        l = r = 0
        for c in s:
            if r == 0 and c == ')':
                l += 1
            else:
                r += 1 if c == '(' else -1
                
        return l + r
        
        
        """
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass
lee215

Intuition:
To make a string valid,
we can add some ( on the left,
and add some ) on the right.
We need to find the number of each.


Explanation:
left records the number of ( we need to add on the left of S.
right records the number of ) we need to add on the right of S,
which equals to the number of current opened parentheses.


Loop char c in the string S:
if (c == '('), we increment right,
if (c == ')'), we decrement right.
When right is already 0, we increment left
Return left + right in the end
                
        """
