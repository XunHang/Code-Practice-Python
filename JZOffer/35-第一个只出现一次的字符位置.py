'''
题目描述:
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个
只出现一次的字符的位置。若为空串，返回-1。位置索引从0开始。

样例输入:
'google'

样例输出:
4

'''
'''
方法一：
建立一个字典，遍历一遍字符串，累计每个字符出现的次数，然后找出
出现次数为1的第一个字符串即可。
【该方法不适用 python2，因为 2 里面字典添加 key 值是无序的】
【比如a = {}; a['a'] = 0; a['b'] = 1; a['c'] = 2; a['d'] = 3
【print a 得到的是：
【{'a': 0, 'c': 2, 'b': 1, 'd': 3}
'''


class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) == 0:
            return -1
        cDict = dict()
        for i in s:
            if cDict.get(i):
                cDict[i] += 1
            else:
                cDict.setdefault(i, 1)

        for k in cDict:
            if cDict[k] == 1:
                return s.index(k)  # index() 用于从列表中找出某个值第一个匹配项的索引位置
        return -1


'''
方法二（太牛逼了）：
利用Python自身的特性，直接利用 list 里的 .count() 方法，
直接统计某个元素在列表中出现的次数，然后返回其索引。
'''


class Solution2:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1


a = 'google'
slt = Solution2()
P = slt.FirstNotRepeatingChar(a)
print(P)
a2 = 'google'
slt2 = Solution2()
P2 = slt.FirstNotRepeatingChar(a2)
print(P2)