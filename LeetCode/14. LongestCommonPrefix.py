'''
Write a function to find the longest common prefix string amongst
an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # zip() 的使用：
        # zip() 可以把列表合并，并创建一个元组对的列表。（长度不同时选最短的）
        # 在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参
        # 数传递给对应函数（前提是对应函数支持不定个数的位置参数）。
        # 本题就用到了这个特性，利用 zip() 来解压缩。
        if not strs:
            return ''
        for i, L in enumerate(zip(*strs)):
            if len(set(L)) != 1:
                return strs[0][:i]
        return min(strs)

    def longestCommonPrefix2(self, strs):
        # 该方法灵活使用了 min()
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


slt = Solution()
a = ["flower", "flow", "flight"]
b = ["dog", "racecar", "car"]
print(slt.longestCommonPrefix(a))
print(slt.longestCommonPrefix2(a))
