class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        """
        Here I use 2 maps, map1 and map2, map1 records the last index for each letter, map2 records the second last index for each letter. They are both initialized as -1(means a letter hasn't shown up) .

        Then consider about introducing a new letter, it will contribute (i - last_ch_position) unique chars, and also decrease (last_ch_position - second_last_ch_position) unique chars.

        Take an example: ABCBB
        i = 0, ch = A, substring = A. A hasn't shown up, so cur += 1, map1:{A:0}, map2:{}
        i = 1, ch = B, substring = AB, B. B hasn't shown up, so cur += 2, map1: {A:0, B:1}, map2:{}
        i = 2, ch = C, substring = ABC, BC, C. cur+= 3, map1:{A:0, B:1, C:2}, map2:{}
        i = 3. ch = B, sustring = ABCB, BCB, CB, B. last_b_position = 1, so it only contributes unique char to the index after last_b_position, which is i-map1[B] = 2, ie CB, B. It also decreases unique char in ABCB and BCB, which is map1[B] - map2[B] = 2, so cur+= 2-2, map1:{A:0, B:3, C:2}, map2:{B:1}
        i = 4, ch = B, substring = ABCBB, BCBB, CBB, BB, B. It increase one unique char which is "B" (i-map1[B]), but decreases 2 unique chars, which are "CBB, BB" (map1[B] - map2[B]), cur += 1 - 2, map1: {A:0, B:4, C:2}, map2:{B:3}
        """
        map1 = collections.defaultdict(lambda:-1)    # last index for this letter
        map2 = collections.defaultdict(lambda:-1)   # second last index for this letter
        cur = 0
        res = 0
        
        for i, ch in enumerate(s):
            cur += (i - map1[ch]) - (map1[ch] - map2[ch])
            map2[ch] = map1[ch]
            map1[ch] = i
            res += cur
        return res        
        
        
        
#         # hard!!!
#         idx = collections.defaultdict(list)
#         for i, c in enumerate(s):
#             idx[c].append(i)
            
#         ans = 0 
#         for arr in idx.values():
#             arr = [-1] + arr + [len(s)]
#             for i in range(1, len(arr) - 1):
#                 ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
#         return ans % (10**9 + 7)