'''
题目描述:
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。

样例输入:
[3, 32, 321]

样例输出:
321323

运行时间：44ms
占用内存：5856k
'''

import operator
from functools import cmp_to_key
'''
方案一：
将所给数的所有组合排列出来，然后进行排序，得到最小的数。
该方案过于暴力且浪费时间空间……
'''


class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ""
        numbers = [str(i) for i in numbers]
        allNumber = self.Permutation(numbers)
        allNumber.sort()
        return allNumber[0]

    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return ss

        pStr = []
        for i in range(len(ss)):
            temp = self.Permutation(ss[:i] + ss[i + 1:])
            for j in list(temp):
                pStr.append(ss[i] + j)

        return pStr


'''
方案二：
自定义一个比较大小的函数，比较两个字符串s1, s2大小
的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大，
如果s1+s2大，那说明s2应该放前面，所以按这个规则，
s2就应该排在s1前面。
'''


def cmp(a, b):
    if (a + b) > (b + a):
        return 1
    elif (a + b) == (b + a):
        return 0
    else:
        return -1


class Solution2:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        # 将数字全部转化为字符串
        numbers = list(map(str, numbers))
        # 使用自定义的排序规则进行排序
        numbers.sort(key=cmp_to_key(cmp))
        if numbers[0] == '0':
            return 0
        else:
            # ''.join实现了字符串之间的连接
            return ''.join(numbers)


a = [3, 32, 321]
slt = Solution()
P = slt.PrintMinNumber(a)
print(P)
b = [3, 32, 321]
slt2 = Solution2()
P2 = slt2.PrintMinNumber(b)
print(P2)
