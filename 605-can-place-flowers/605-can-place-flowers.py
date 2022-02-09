class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # https://leetcode.com/problems/can-place-flowers/discuss/184330/Python-easy-solution-beats-100
        # We can put one flower in every three contingous empty spots, 
        # after put that flower in the middle of three, t
        # he thrid one can be counted into the "next three spots". So we set the count variable to be 1.
        # Since the head and the tail are special cases, we insert a empty spot at head and append a empty spot at the tail.
        
        bed = [0] + flowerbed + [0] # same as flowerbed.insert(0, 0), flowerbed.append(0)
        
        # bed length n+2 (idx 0 to n+1), traverse from bed[1] to bed[n]
        for i in range(1, len(flowerbed)+1):  
            if bed[i - 1] == bed[i] == bed[i + 1] == 0:
                bed[i] = 1
                n -= 1
        
        return n <= 0 # if n <= 0, return True