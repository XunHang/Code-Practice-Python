'''
题目描述:
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

样例输入:
10

样例输出:
12

'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        # 前六个正整数均为丑数（1，2，3，4，5，6）
        if index < 7:
            return index
        # 任何一个丑数，都是由之前的某个丑数 a 通过乘2/3/5得到的，也就是 a*2 或 a*3 或 a*5；
        # 所以我们认为下一个丑数是由：
        # 【第 t2 个丑数乘 2 / 第 t5 个丑数乘 5 / 第 t5 个丑数乘 5】得到的；
        # 同时，我们不知道下一个丑数是哪个丑数乘几得到的，只知道丑数是顺序排列的；
        # 因此我们把所有丑数分为 t2/t3/t5 三类，如果当前这个丑数是由之前某个丑数乘 n 得到
        # 的，那么 tn 就加 1，以此作为索引，将三个序列合围一个。
        uglyNumber = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(index-1):
            uglyNumber.append(
                min(uglyNumber[t2] * 2, 
                    uglyNumber[t3] * 3,
                    uglyNumber[t5] * 5))
            # 都用 if 是因为有些数（比如6）可以同时满足 丑数3*2所得和丑数2*3所得.
            if uglyNumber[i + 1] == uglyNumber[t2] * 2:
                t2 = t2 + 1
            if uglyNumber[i + 1] == uglyNumber[t3] * 3:
                t3 = t3 + 1
            if uglyNumber[i + 1] == uglyNumber[t5] * 5:
                t5 = t5 + 1

        return uglyNumber[-1]


a = 10
slt = Solution()
P = slt.GetUglyNumber_Solution(a)
print(P)
