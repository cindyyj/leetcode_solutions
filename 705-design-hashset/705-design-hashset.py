class MyHashSet:
    # BST as bucket
    def __init__(self):
        self.set = [False] * 1000001        

    def add(self, key: int) -> None:
        self.set[key] = True
        
    def remove(self, key: int) -> None:
        self.set[key] = False        

    def contains(self, key: int) -> bool:
        return self.set[key]



    """
1. 超大数组
能使用超大数组来解决本题是因为输入数据的范围在 0 <= key <= 10^60<=key<=10^6
因此我们只需要 10^6 + 1大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。

因为对于 HashSet 来说，我们只需要关注一个 key 是否存在，而不是 key:value 形式的 HashMap，因此，我们把数组的元素设计成 bool 型的，当某个 key 的对应的数组中的位置取值为 true 说明该 key 存在，取值为 false，说明该 key 不存在。

优点：查找和删除的性能非常快，只用访问 1 次数组；
缺点：使用了非常大的空间，当元素范围很大时，无法使用该方法；当存储的元素个数较少时，性价比极低；需要预知数据的取值范围。

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/design-hashset/solution/xiang-jie-hashset-de-she-ji-zai-shi-jian-4plc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    """
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)