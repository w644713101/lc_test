"""
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。

你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。
每采摘一次，你将会向右移动到下一棵树，并继续采摘。

一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。



示例 1：
输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。

示例 2：
输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。

示例 3：
输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。

示例 4：
输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。


提示：

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

链接：https://leetcode.cn/problems/fruit-into-baskets

"""
from collections import Counter

if __name__ == '__main__':
    fruits = [1,0,29,29,29,29,29,29,0,0,29,8,8,29,8,29,8,8,15,8,8,15,15,8,15,15,8,8,7,5]
    """官方"""
    cnt = Counter()

    left = ans = 0
    for right, x in enumerate(fruits):
        cnt[x] += 1
        while len(cnt) > 2:
            cnt[fruits[left]] -= 1
            if cnt[fruits[left]] == 0:
                cnt.pop(fruits[left])
            left += 1
        ans = max(ans, right - left + 1)

    import pdb;pdb.set_trace()
    """我自己"""
    before = None
    now = None
    q = [0, 0]
    max_sum = 0
    middle_flag = 0
    for index, value in enumerate(fruits):
        if not before and not value and not isinstance(now, int) and not isinstance(before, int):
            now = value
            q[0] += 1
        elif now == value:
            q[0] += 1
            if middle_flag:
                middle_flag += 1
        elif before == value:
            q[1] += 1
            tmp = q[0]
            q[0] = q[1]
            q[1] = tmp
            before = now
            now = value
            middle_flag = 1
        else:
            max_sum = max_sum if q[0]+q[1] < max_sum else q[0]+q[1]
            before = now
            q[1] = q[0] if not middle_flag else middle_flag
            now = value
            q[0] = 1
            middle_flag = 0
        print(max_sum)
    else:
        max_sum = max_sum if q[0] + q[1] < max_sum else q[0] + q[1]

    print(max_sum)

