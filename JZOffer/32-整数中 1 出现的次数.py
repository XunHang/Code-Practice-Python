'''
题目描述:
1~13中包含1的数字有1、10、11、12、13因此共出现6次,试写出一个算
法，可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出
现的次数）。

样例输入:
13

样例输出:
6

运行时间：44ms
占用内存：5856k
'''


class Solution:
    # 使用暴力解法，复杂度为 O(n*logn)
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        while n != 0:
            count = count + self.NumberOf1(n)
            n = n - 1
        return count

    # 判断当前数字有几位为 1
    def NumberOf1(self, number):
        self.counter = 0
        while number != 0:
            if number % 10 == 1:
                self.counter = self.counter + 1
            number = number // 10
        return self.counter


a = 13
slt = Solution()
P = slt.NumberOf1Between1AndN_Solution(a)
print(P)
