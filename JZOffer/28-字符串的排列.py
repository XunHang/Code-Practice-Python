'''
题目描述:
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
注意 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母

样例输入:
abc

样例输出:
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

'''


class Solution:
    def Permutation(self, ss):

        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        pStr = []
        for i in range(len(ss)):
            if i > 0 and ss[i] == ss[i - 1]:
                continue
            temp = self.Permutation(ss[:i] + ss[i + 1:])
            for j in temp:
                pStr.append(ss[i] + j)

        return pStr


a = 'abc'
slt = Solution()
P = slt.Permutation(a)
print(P)