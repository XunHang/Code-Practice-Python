'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321
Example 2:
    Input: -123
    Output: -321
Example 3:
    Input: 120
    Output: 21
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        signed = 1 if x > 0 else -1
        r = signed * int(str(abs(x))[::-1])
        if r >= (2**31) or r < -(2**31):
            return 0
        else:
            return r


slt = Solution()
print(slt.reverse(123))
print(slt.reverse(-123))
print(slt.reverse(120))
