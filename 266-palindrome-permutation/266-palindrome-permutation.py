class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        SingleNumber only works if nums comes in pairs except one, here the string maybe like "hello" with more than one single number.

        Finally get it! super smart idea. due to the limit of 26 chars, 
        the key is to convert it to the binary number where the position in binary number corresponds to the alphabet
        Basically with 1 << (ord(c) - ord('a')) , for example, 'a' --> 0b1, 'b' --> 0b10, 'c' --> 0b100, really really smart.

        Then xor can flip the bit.
        You'd use a bit mask of all 1s for XOR
        1 ^ 1 = 0
        0 ^ 1 = 1        
        xor can flip the bit when seen twice
        
        Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0 to judge whether that is the case
        
        """
        # Since we have at most 26 characters in the English lowercase alphabet, 
        # we can maintain a binary number that represents if a corresponding character is seen an odd/even number of times. 
        # We use XOR to flip the bit. At the end, we use what we learn from the problem named power of 2, to check if we have only 1
              
        isOdd = 0
        for c in s:
            isOdd ^= 1 << (ord(c) - ord('a'))
        return isOdd & (isOdd - 1) == 0 
        
# # -------------------- METHOD 4 : hashmap --------------------------- 
#         # TC O(n) n is the number of the character of string
#         # SC O(1) the maximum size of the set would be 128 ASCII characters
#         # This is bounded (constant)
    
#         odds = set()
        
#         for char in s:
#             if char not in odds:
#                 odds.add(char)
#             else:
#                 odds.remove(char)
        
#         return len(odds) <= 1
        
# # --------------------------- METHOD 3: Counter ---------------------------                
#         return sum(v % 2 for v in Counter(s).values()) < 2

    
# # --------------------------- METHOD 2 ---------------------------        
        
#         counts = collections.Counter(s)
#         odds = [cnt for cnt in counts.values() if cnt & 1]  # num & 1 same as num % 2 == 1
        
#         return len(odds) <= 1
        
# # --------------------------- METHOD 1 ---------------------------        
#         counts = collections.Counter(s)
#         nums = counts.values()
        
#         odds = even = 0
#         for num in nums:
#             if num & 1:
#                 odds += 1
#             else:
#                 even += 1
        
#         return odds <= 1