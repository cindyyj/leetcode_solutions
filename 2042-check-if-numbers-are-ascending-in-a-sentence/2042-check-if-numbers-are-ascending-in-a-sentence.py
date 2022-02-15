class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split(' ')
        nums = []
        for word in arr:
            if word.isdigit():
                nums.append(int(word))
                
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))