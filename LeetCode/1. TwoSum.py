'''
Given an array of integers, return indices of the two
numbers such that they add up to a specific target.
You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


# 时间复杂度 O(n)，最大耗时 2n
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i

        for j in range(len(nums)):
            # if dict[target - nums[j]]:  的这种写法是不可以
            # 的，因为这个 key 有可能不存在（比如测试样例 1下
            # 得到的 dict={2:0, 5:2, 11:3}，重复元素会被覆盖
            # 掉。但是因为第二次遍历的是 nums，所以不会遗漏什
            # 么，依然可以得到正确答案。
            if (target - nums[j]) in dict:
                if j != dict[target - nums[j]]:
                    return [j, dict[target - nums[j]]]
                # 如果不加这个判断条件，则测试样例 2 下的返回
                # 值则为 [0, 0]，因此要排除这种自身×2得到目标
                # 值的错误情况。
                else:
                    pass


# 时间复杂度 O(n)，最大耗时 n
# 在该方法下，就不用判断组成 target 值的两个数是不是同一元素了
class Solution2:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i


slt = Solution()
slt2 = Solution2()
nums = [2, 5, 5, 11]
target = 10
print(slt.twoSum(nums, target))
print(slt2.twoSum(nums, target))
nums_2 = [3, 2, 4]
target_2 = 6
print(slt.twoSum(nums_2, target_2))
print(slt2.twoSum(nums_2, target_2))
