'''
题目描述:
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,
他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向
量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某
个负数,并期望旁边的正数会弥补它呢？
给一个数组，返回它的最大连续子序列的和(子向量的长度至少是1)

样例输入:
[6,-3,-2,7,-15,1,2,2]

样例输出:
8
'''


class Solution:
    # 改题目使用动态规划，设前 i 个数的和为 f(i)，
    # 则如果 f(i) < 0，则 f(i+1) < attay[i+1]，
    # 因此此时应该直接令 f(i+1) = attay[i+1]。
    # 即：
    #        ┌ array[i+1]           f(i)<0 or i = 0
    # f(x) = ┤
    #        └ f(i) + array[i+1]    f(i)>0 and i ≠ 0
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0:
            return 0
        sumA = array[0]
        maxA = sumA
        for i in array[1:]:
            if sumA >= 0:
                sumA = sumA + i
            else:
                sumA = i
            if sumA > maxA:
                maxA = sumA
        return maxA


a = [6, -3, -2, 7, -15, 1, 2, 2]
slt = Solution()
P = slt.FindGreatestSumOfSubArray(a)
print(P)
