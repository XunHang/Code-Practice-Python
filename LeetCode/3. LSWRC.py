'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest 
substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) is 0:
            return 0
        maxLength = 0
        s_out = ''
        for i in s:
            if i not in s_out:
                s_out = s_out + i
            else:
                if len(s_out) > maxLength:
                    maxLength = len(s_out)
                s_out = s_out[(s_out.find(i)+1):] + i
        if len(s_out) > maxLength:
            maxLength = len(s_out)
        return maxLength


slt = Solution()
s = ' '
print(slt.lengthOfLongestSubstring(s))