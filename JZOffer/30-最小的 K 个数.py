'''
题目描述:
输入n个整数，找出其中最小的K个数。

样例输入:
4,5,1,6,2,7,3,8

样例输出:
1,2,3,4
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == [] or k > len(tinput):
            return []
        # 利用 set 完成去重与排序，然后转化为 list 后输出
        T = list(set(tinput))
        return T[:k]


a = [4, 5, 1, 6, 2, 7, 3, 8]
slt = Solution()
P = slt.GetLeastNumbers_Solution(a, 4)
print(P)
