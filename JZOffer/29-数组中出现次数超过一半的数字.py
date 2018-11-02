'''
题目描述:
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。

样例输入:
1 2 3 2 2 2 5 4 2

样例输出:
2
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 利用归并排序将列表变为有序列表
        numbers.sort()
        # 通过将列表转化为 set，去除重复元素
        N = set(numbers)
        # 如果元素类别太多，不足以有任何一个元素数量大于总数的一半，则返回 0
        if ((len(numbers) + 1) / len(N) < 2):
            return 0
        # 如果众数存在，一定是排序后处于中间的那个数
        mode = numbers[(len(numbers) - 1) // 2]
        counter = 0
        # 通过一次遍历，判断 mode 的数量是否大于总数的一半
        for i in numbers:
            if i == mode:
                counter = counter + 1
                if counter == (len(numbers) + 1) // 2:
                    return mode
        return 0


a = [1, 2, 3, 2, 2, 2, 5, 4, 2]
slt = Solution()
P = slt.MoreThanHalfNum_Solution(a)
print(P)
