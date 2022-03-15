class Solution:
    def makeFancyString(self, s: str) -> str:
        
        # two pointer
        res = ""
        cnt, k = 0, 3
        for i, c in enumerate(s):
            if i > 0 and s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < k:
                res += c
        return res

    
        # # wrong solution!
        # # this will make "leeetcode" - >"leetcod" 
        # # last "e" got deleted as there are 4 "e"s, only need to delete 3+ consecutive characters
        # # if not consecutive, no need to delete!
        # while i < len(s):
        #     d[s[i]] += 1
        #     if d[s[i]] < k:
        #         res += s[i]
        #     i += 1        
        # return res