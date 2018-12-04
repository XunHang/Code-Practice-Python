class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = '1'
        while n - 1:
            print(r)
            temp = ''
            lenn = len(r)
            i = 0
            while lenn - i:
                count = 0
                if len(r[i:]) == 1:
                    temp += '1' + r[-1]
                else:
                    cur = r[i]
                    for j in r[i:]:
                        if j != cur:
                            break
                        count += 1
                    i += count - 1
                    temp += str(count) + cur
                i += 1
            r = temp
            n -= 1
        return r


slt = Solution()
print(slt.countAndSay(5))
