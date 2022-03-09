class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        d = {0:0, 1:1, 6:9, 9:6, 8:8}
        nums = list(map(int, str(n)))
        new_n = list()
        
        for num in nums:
            if num not in d:
                return False
            else:
                new_n.append(d[num])
        
        return new_n[::-1] != nums
        
        
#         rotation = {"0": 0, "1": 1, "6": 9, "8": 8, "9": 6}
#         num = 0

#         for i, ch in enumerate(str(n)):
#             if ch not in rotation:
#                 return False
#             else:
#                 num += rotation[ch] * 10 ** i

#         return num != n