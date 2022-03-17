class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # list_ = []
        # products.sort()
        # for i, c in enumerate(searchWord):
        #     products = [ p for p in products if len(p) > i and p[i] == c ]
        #     list_.append(products[:3])
        # return list_
        
        
        
        # lexicographically 
        products.sort()
        query = ""
        ans = list()
        
        def binary_search(array, target): # bisect.bisect_left implementation
            lo = 0
            hi = len(array)

            while lo < hi:
                mid = (lo + hi) //2
                if array[mid] < target: 
                    lo = mid + 1
                else: hi = mid
            
            return lo
             
        for ch in searchWord:
            query += ch
            find = binary_search(products, query) # bisect.bisect_left
            ans.append([s for s in products[find: find + 3] if s.startswith(query)])
            last = find
        
        return ans
        
        """
        My Thoughts:

Key points that could be applied to other problems:
'Lexographical': This should hint you the data requires some ordering between them. Sort!!
'Compute after each character of searchWord is typed': This should hint you to carefully elimiate some data (thus reducing search space) during each character computation. Here, Two pointer/Binary Search/Trie
Medium vs Hard:
Comping up with BS and Trie approaches, analayzing their time ans dpace complexities, designing the modular functions and implementingthe code, each in itself should be labelled HARD. There's a more simpler approach Sort+2 Pointer which might seem a medium, but only if you don't discuss about the Trie and BS approaches (because interviewer would gruel on time and space before asking to pick one)
LC approach 1 says "Here we treat string comparison in sorting as O(1)": WHY?
Shouldn't it be number of characters in the largest product? Please check https://stackoverflow.com/a/64575094
LC time in ms:
From Java accepted submissions, 'Sort with 2 Pointer' approach is 6 ms. 'Sort with Binary Search' approach is 16 ms and Trie with DFS is 148 ms. Why this big variation between approaches? It is understandable that Big O is just a theoretical term and time complexities vary in practical scenarios, but then at-least the test cases should be modified to decrease the huge difference in time complexities between these three approaches, so users will implement the right approach during interviews. Please clearly suggest which approach a candidate should discuss with the interviewer for this problem and which approach he/she should code in interview.
Time complexities:
Let, m = searchWord length, n = products array length, p = largest product word length
Sort with 2 Pointer: O(p * nlogn) + O(n) + O(m * 3p) | ie, Arrays.sort() + 2 Pointer on shortened array (note: 2 Pointer "for each character of searchWord" isn't relevant here as n elements are visted only once) + Add 3 products to list for every letter of search word
Sort with Binary Search: O(p * nlogn) + O(m * (logn + 3p)) | ie, Arrays.sort() + Binary Search and .substring() Comparison on 3 products for each character of searchWord.
Trie with backtrack: O(p * n) + O(m * 3p) | ie, Build Trie + backtrack for 3 products for every letter of search word
Codes: https://leetcode.com/problems/search-suggestions-system/discuss/1024115/Lessons-learned

Conclusion:
I think for time complexity, it all depends on which is greater: 'm' vs 'n'. If 'm', Trie is worst. If 'n', Trie is best. But in interview, I would code 2 pointer first (better than binary search in time complexity and simpler to code) and then discuss about Trie and also discuss about time complexities.

Update:

"Sort+Binary search' approach can also be implemented with two pointers similar to https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array . Time and space complexity remains same.
Advantages:
a) Reduces right side of search space
b) Single character comparison instead of prefix String comparison for each letter of searchWord.
An advanced version of this problem where frequencies are included along with lexographiclal order: https://leetcode.com/problems/design-search-autocomplete-system/
        
        """