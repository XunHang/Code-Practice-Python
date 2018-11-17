'''
题目描述:
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
【题目保证输入的数组中没有的相同的数字】

样例输入:
1,2,3,4,5,6,7,0

样例输出:
7

'''


# 排序过程，就是一个不断地消除逆序对的过程，而归并排序中，合并过程就是
# 不断消除逆序对的过程，并且其时间复杂度为 O(nlogn)，比O(n^2)小得多。
# Ps. 牛客的时间限制下，使用 Python 无论如何也不能通过测试（sad）
class Solution:
    def merge(self, a, b):  #a,b是待合并的两个列表,两个列表分别都是有序的，合并后才会有序
        global count
        merged = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                count += 1
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    #递归操作
    def merge_sort(self, c):
        if len(c) <= 1:
            return c
        mid = len(c) // 2  # 除法取整
        a = self.merge_sort(c[:mid])
        b = self.merge_sort(c[mid:])
        return self.merge(a, b)

    def InversePairs(self, data):
        length = len(data)
        if length <= 0:
            return 0

        self.merge_sort(data)

        return count % 10000000007


class Solution2:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        if length <= 0:
            return 0
        copy = [0] * length
        # 下面这步很关键，不然的话返回的结果就是 3
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count % 10000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        # 对两个数组进行对比取值的过程
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 剩下的一个数组未取完的操作
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count


count = 0
a = [1, 2, 3, 4, 5, 0]
slt = Solution2()
P = slt.InversePairs(a)
print(P)
