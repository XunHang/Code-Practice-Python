class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        n_l = len(needle)
        if len(haystack) < n_l:
            return -1
        for i in range(len(haystack)):
            if len(haystack[i:-1]) < n_l:
                return -1
            if haystack[i:i + n_l] == needle:
                return i


slt = Solution()
a = "miss"
b = 'a'
print(slt.strStr(a, b))
