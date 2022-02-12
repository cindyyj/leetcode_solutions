# # --------------------------- METHOD 2 ---------------------------
# 时间复杂度：O(N/b)，N 是元素个数，b 是桶数。
# 空间复杂度：O(N)

class MyHashSet:
    # 不定长拉链数组
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        self.table = [[None] * self.cap]
        
    def hash(self, key):
        return key % self.cap

    def add(self, key):
        if self.contains(key):
            return
        hashkey = self.hash(key)
        self.table[hashkey].append(key)

    def remove(self, key):
        if not self.contains(key):
            return        
        hash_key = self.hash(key)
        self.table[hash_key].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]

# # --------------------------- METHOD 1 ---------------------------

    """
2. 不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。

分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。

优点：节省内存，不用预知数据范围；
缺点：在链表中查找元素需要遍历。


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

class MyHashSet:
    # large array as bucket
    def __init__(self):
        self.set = [False] * 1000001        

    def add(self, key: int) -> None:
        self.set[key] = True
        
    def remove(self, key: int) -> None:
        self.set[key] = False        

    def contains(self, key: int) -> bool:
        return self.set[key]
    
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



# complicate one, using BST
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key) -> int:
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Bucket:
    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.val:
            return root
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root

    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
