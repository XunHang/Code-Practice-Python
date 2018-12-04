class Solution:
    def plusOne(self, D):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = 1
        while (carry):
            if (i > len(D)):
                D = [1] + D
                carry = 0
            else:
                temp = D[-i]
                D[-i] = (D[-i] + carry) % 10
                carry = (temp + carry) // 10
                i += 1
        return D


slt = Solution()
d = [9, 9]
print(slt.plusOne(d))
