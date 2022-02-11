from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        count1 = Counter(s1)
        count2 = Counter()
        
        start = 0
        for end in range(l2):
            count2[s2[end]] += 1
            
            if end >= l1:
                count2[s2[start]] -= 1
                if count2[s2[start]] == 0:
                    del count2[s2[start]]
                start += 1
            
            if count1 == count2:
                return True
        
        return False

        
# # --------------------------- METHOD 2 ---------------------------
        
#         # two pointer
#         l1, l2 = len(s1), len(s2)
#         if l1 > l2:
#             return False
        
#         count1 = Counter(s1)
#         count2 = Counter()
        
#         for i in range(l2):
#             count2[s2[i]] += 1
#             if i >= l1: 
#                 count2[s2[i - l1]] -= 1
            
#             if count1 == count2:
#                 return True
            
#         return False

# # --------------------------- METHOD 1 ---------------------------
#         # sliding window
#         # https://leetcode.com/problems/minimum-window-substring/
#         # https://leetcode.com/problems/longest-substring-without-repeating-characters/
#         # https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#         # https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#         # https://leetcode.com/problems/find-all-anagrams-in-a-string/        
        
#         if len(s1) > len(s2):
#             return False
        
#         count1 = Counter(s1)
#         for i in range(len(s2) - len(s1) + 1): 
#             if count1 == Counter(s2[i: i+len(s1)]):
#                 return True
        
#         return False