'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
    Input: "(]"
    Output: false
Example 2:
    Input: "{[]}"
    Output: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        dictt = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            elif not dictt[i] + dictt[stack[-1]]:
                stack.pop()
            else:
                stack.append(i)
        return not bool(len(stack))

    # 下麦你这个解决方案更为优秀，比上面方法多利用了左右括号出现的顺序性
    def isValid_Better(self, s):
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


slt = Solution()
a = "(]"
b = "{[]}"
c = "()[]{}"
print(slt.isValid(a))
print(slt.isValid(b))
print(slt.isValid(c))
