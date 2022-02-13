class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = collections.defaultdict(list)
        
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            d[tuple(counts)].append(s)
            
        return d.values()
                
        
        
#         # --------------------------- METHOD 1 ---------------------------
#         # Categorize by Sorted String
#         # time: O(N*KlogK), k max length of string in strs. N, number of strings in strs
#         # space: O(N * k), total info stored in ans
#         ans = defaultdict(list)
#         for s in strs:
#             key = tuple(sorted(s))
#             ans[key].append(s)
#         return ans.values()
        
#         # sorted string w. built-in functions
#         ans = {}
#         for s in strs:
#             key = tuple(sorted(s))
#             ans[key] = ans.get(key, []) + [s]
#         return ans.values()