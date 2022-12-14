"""
我们构建了一个包含 n 行(索引从 1 开始)的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
给定行数n和序数 k，返回第 n 行中第 k个字符。（k从索引 1 开始）


示例 1:
输入: n = 1, k = 1
输出: 0
解释: 第一行：0

示例 2:
输入: n = 2, k = 1
输出: 0
解释:
第一行: 0
第二行: 01

示例 3:
输入: n = 2, k = 2
输出: 1
解释:
第一行: 0
第二行: 01


提示:
1 <= n <= 30
1 <= k <= 2n - 1


链接：https://leetcode.cn/problems/k-th-symbol-in-grammar

"""
import math
if __name__ == '__main__':
    n = 3
    k = 3
    floor = math.pow(2, n-1)
    all_node = math.pow(2, n) - 1
    find_node = all_node - floor + k
    parity = []
    now = find_node
    for _ in range(n-1):
        parity.append(int(now%2))
        now = int(now/2)
    zero_map = {"0": 0, "1": 1}
    one_map = {"0": 1, "1": 0}
    res_value = 0
    parity.reverse()
    for value in parity:
        if res_value == 0:
            res_value = zero_map[str(value)]
        else:
            res_value = one_map[str(value)]

    print(res_value)



