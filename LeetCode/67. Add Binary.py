class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        summ = ''
        carry = 0  # 定义进位
        l1 = len(a)
        l2 = len(b)
        while (l1 or l2 or carry):
            if l1 > 0:
                if a[l1 - 1] == '1':
                    carry += 1
            if l2 > 0:
                if b[l2 - 1] == '1':
                    carry += 1
            summ = str(carry % 2) + summ
            carry = carry // 2
            l1 -= 1 if l1 > 0 else 0
            l2 -= 1 if l2 > 0 else 0

        return summ


slt = Solution()
a = '10'
b = '1'
print(slt.addBinary(a, b))
