class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # # Categorize by Sorted String
        # # time: O(N*KlogK), k max length of string in strs. N, number of strings in strs
        # # space: O(N * k), total info stored in ans
        # ans = defaultdict(list)
        # for s in strs:
        #     key = tuple(sorted(s))
        #     ans[key].append(s)
        # return ans.values()
        
        ans = {}
        for s in strs:
            key = tuple(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return ans.values()