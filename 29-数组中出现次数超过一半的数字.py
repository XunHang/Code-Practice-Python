'''
题目描述:
输入一个字符串,按字典序打印出该字符串中字符的所有排列
例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
注意 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母

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
