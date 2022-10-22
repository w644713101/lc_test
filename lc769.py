"""
769. 最多能完成排序的块

给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。


示例 1:
输入: arr = [4,3,2,1,0]
输出: 1
解释:
    将数组分成2块或者更多块，都无法得到所需的结果。
    例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。


示例 2:
输入: arr = [1,0,2,3,4]
输出: 4
解释:
    我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
    然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。

提示:
    n == arr.length
    1 <= n <= 10
    0 <= arr[i] < n
    arr中每个元素都 不同

[1,2,0,3] 2
[2,0,1] 1
[4,3,2,1,0] 1
[1,0,2,3,4] 4
[1,2,3,4,5,0] 1
[2,0,1,3] 2
[0,4,5,2,1,3] 2
[1,4,3,6,0,7,8,2,5] 1
链接：https://leetcode.cn/problems/max-chunks-to-make-sorted
"""

# if __name__ == '__main__':
#     arr: list = [1,2,0,3]
#     res = 0
#     flag = False
#     max_value = 0
#     min_value = 0
#     min_flag = False
#     res_sum = 0
#     for index, value in enumerate(arr):
#         res_sum += value
#         find_index = index + 1 if index != len(arr) - 1 else index
#         max_value = value if value > max_value else max_value
#         if min_value == value:
#             min_flag = True
#         if min_flag and res_sum == ((max_value+1)*max_value)/2:
#             min_value = max_value+1
#             min_flag = False
#             res += 1
#             flag = False
#         else:
#             flag = True
#     res = res+1 if flag else res
#     print(res)

if __name__ == '__main__':
    arr = [1,4,3,6,0,7,8,2,5]
    ans = mx = 0
    for i, x in enumerate(arr):
        mx = max(mx, x)
        import pdb;pdb.set_trace()
        ans += mx == i
    print(ans)

