class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.abbre(word)
            self.d[abbr].add(word)

    def abbre(self, word):
        return word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word

    def isUnique(self, word):
        abbr = self.abbre(word) 
        if abbr not in self.d:
            return True
        return len(self.d[abbr]) == 1 and word == list(self.d[abbr])[0]
    

"""
https://leetcode.com/problems/unique-word-abbreviation/discuss/149925/Python-or-tm

这题题目不难，但题目定义的让我一脸懵逼。
就是给了一组List，里面有若干个英语单词。然后除去头和尾，其他的字符都缩成了数字，比如：
"dear"的头是d，尾巴是r，中间的ea一共是2个字母，所以变成了2，最终缩完的output是：d2r

主方程isUnique()的判定条件是

缩写完以后的input是否出现在字典中过，如果没出现过，则代表字典不包含当前input，则返回True。

如果出现过，继续比对两个缩写单词的原词，举例：
比如dear和door缩写完以后都为d2r，虽然在字典里的key同为d2r，但实际原词不一样
如果原词一样，则表示这个单词任然是Unique，因为字典里包含的就是原词本身。
如果不一样，则代表字典里有其他缩写相等的词，返回False

# if word abbreviation not in the dictionary
# or word itself in the dictionary (word itself may appear multiple times in the dictionary)
# so it's better using set instead of list)    
"""
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)