"""

给定一个整数数组 arr，找到 min(b)的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。



示例 1：
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

示例 2：
输入：arr = [11,81,94,43,3]
输出：444


提示：
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104


链接：https://leetcode.cn/problems/sum-of-subarray-minimums
"""
from typing import List

"""no"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        """myself timeout"""
        before_num = arr[0]
        cache_map = {f'{str(arr[0])}_0': [arr[0], ]}  # list 存最小的数
        res_sum = arr[0]
        for i in range(1, len(arr)):
            value = arr[i]
            cache_map[f'{str(value)}_{str(i)}'] = [value, ]
            res_sum += value
            before_cache = cache_map[f'{str(before_num)}_{str(i-1)}']
            tmp_cache = []
            for index, cur_min in enumerate(before_cache):
                this_min = min(cur_min, value)
                tmp_cache.append(this_min)
                res_sum += this_min
                cache_map[f'{str(value)}_{str(i)}'].append(this_min)
            cache_map[f'{str(before_num)}_{str(i-1)}'] = tmp_cache
            before_num = value
        # return res_sum % MOD
        return res_sum


if __name__ == '__main__':
    arr_list = [[3,1,2,4], [11,81,94,43,3], [19,19,62,66]]
    t = Solution()
    for arr in arr_list:
        print(f'res is {t.sumSubarrayMins(arr)}')