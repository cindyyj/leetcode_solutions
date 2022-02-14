class TwoSum:

    def __init__(self):
        self.cache = defaultdict(int)

    def add(self, number: int) -> None:
        self.cache[number] += 1

    def find(self, value: int) -> bool:
        for num in self.cache:
            complement = value - num
            if complement in self.cache:
                if complement != num or (complement == num and self.cache[num] >= 2):
                    return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

