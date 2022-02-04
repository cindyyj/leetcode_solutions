class ProductOfNumbers:

    def __init__(self):
        self.arr =[]
        self.prefix = [1]

    def add(self, num: int) -> None:
        self.arr.append(num)
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0

        return self.prefix[-1] // self.prefix[-1 - k]
        

        '''
        Logic:
Initialize an array with value 1 and is used to store the prefix product.
Whenever a new number is added, append the prefix with (prefix[-1] x num)
Product of last k numbers would be (prefix[-1] // prefix[-1-k])
The above algorithm will work fine iff 0 is never encountered.
To accommodate 0 also, we need to slightly tweak the algorithm.
Let us say that whenever 0 is encountered, prefix reinitialize with [1] and again prefix product is calculated for next numbers.
And now when the prod of last k elements is needed, we can check whether the length of prefix is greater than or equal to k.

If it is then the above formula will work to get the product.
Else, simply return 0 because there must be atleast one 0 in last k elements and that is why the length of prefix is less than k.
        '''

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)