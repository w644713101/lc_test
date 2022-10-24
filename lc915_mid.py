"""
给定一个数组nums，将其划分为两个连续子数组left和right，使得：

left中的每个元素都小于或等于right中的每个元素。
left 和right都是非空的。
left 的长度要尽可能小。
在完成这样的分组后返回left的长度。

用例可以保证存在这样的划分方法。



示例 1：

输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
示例 2：

输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]


提示：

2 <= nums.length <= 105
0 <= nums[i] <= 106
可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。

链接：https://leetcode.cn/problems/partition-array-into-disjoint-intervals
[32,57,24,19,0,24,49,67,87,87]  未及时更新左面的最大值
[24,11,49,80,63,8,61,22,73,85]  检查右面的的时候，对右面最大值进行调整
[1,1] 题干是大于等于
"""

if __name__ == '__main__':
    """official"""
    nums = [90,47,69,10,43,92,31,73,61,97]
    n = len(nums)
    cur_max = left_max = nums[0]
    left_pos = 0
    for i in range(1, n - 1):
       cur_max = max(cur_max, nums[i])
       if nums[i] < left_max:
           left_max, left_pos = cur_max, i
    print(left_pos + 1)

    """myself"""
    max_left = 0
    max_right = 0
    len_left = 0
    i = 0
    while i < len(nums)-1:
        max_left = nums[i] if nums[i] > max_left else max_left
        print(f'i is {i}')
        print(f'max_left is {max_left}')
        if max_left < nums[i+1]:  # left<right, need judge right
            j = i+1
            flag = True
            while j < len(nums):
                max_right = nums[j] if nums[j] > max_right else max_right
                print(f'j is {j}')
                print(f'max_right is {max_right}')
                if nums[j] > max_left:
                    j += 1
                    continue
                else:
                    # max_left = max_right if max_right > max_left else max_left
                    max_left = max_right
                    flag = False
                    i = j
                    max_right = 0
                    break
            if flag:
                break
        else:
            i += 1
    print(f'res is {i+1}')


