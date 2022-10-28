"""
已知函数signFunc(x) 将会根据 x 的正负返回特定值：

如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

返回 signFunc(product) 。


示例 1：
输入：nums = [-1,-2,-3,-4,3,2,1]
输出：1
解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1

示例 2：
输入：nums = [1,5,0,2,-3]
输出：0
解释：数组中所有值的乘积是 0 ，且 signFunc(0) = 0

示例 3：
输入：nums = [-1,1,-1,1,-1]
输出：-1
解释：数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1


提示：
    1 <= nums.length <= 1000
    -100 <= nums[i] <= 100

链接：https://leetcode.cn/problems/sign-of-the-product-of-an-array
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """office"""
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
       # return sign

        """cool"""
        res = 0 if nums.count(0) > 0 else 1 if sum(s < 0 for s in nums) % 2 == 0 else -1

        """myself"""
        little_sum = 0
        if 0 in nums:
            return 0
        else:
            for value in nums:
                if value < 0:
                    little_sum += 1
        if little_sum % 2 == 1:
            return -1
        else:
            return 1



if __name__ == '__main__':
    nums_list = [[-1,-2,-3,-4,3,2,1], [1,5,0,2,-3], [-1,1,-1,1,-1]]
    for nums in nums_list:
        s = Solution()
        print(f'res is {s.arraySign(nums)}')