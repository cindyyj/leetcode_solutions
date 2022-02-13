class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Categorize by Sorted String
        # time: O(N*KlogK), k max length of string in strs. N, number of strings in strs
        # space: O(N * k)
        ans = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            ans[key].append(s)
        return ans.values()
        