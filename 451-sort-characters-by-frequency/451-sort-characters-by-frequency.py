from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # use built-in function only 
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # sort_freq = sorted(freq, key=freq.get, reverse=True)
        # return ''.join(char * freq[char] for char in sort_freq)
    
#         # sort_freq here is a sorted tuple (key, value)
#         sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#         return ''.join(x[0] * x[1] for x in sort_freq)
    
        sort_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        return ''.join(x[0] * x[1] for x in sort_freq.items())      

        
        # using Counter 
        # time O(nlogn), space O(n)
        # Strings are Immutable!
        counts = Counter(s)
        
        # rebuild the string
        res = []
        for char, freq in counts.most_common():
            res.append(char * freq)
        
        return ''.join(res)
        