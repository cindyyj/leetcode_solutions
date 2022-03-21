class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # To have GCD substring, the length of it has to be a GCD of len(s1) and len(s2)
        # Check if s1 + s2 == s2 + s1 to make sure such a string exists
        # Unfortunately in Python slicing a list is linear time instead of constant time, O(n1+n2):
        
        # return str1[:math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""
        
        n1 = len(str1)
        n2 = len(str2)        
        # check if both strings contain same repeating vals
        if str1+str2 != str2+str1:
            return ""
        if str1 == str2:
            return str1
        return str1[:gcd( n1, n2 )]