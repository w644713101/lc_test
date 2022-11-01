"""

给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
返回必须翻转的 0 的最小数目。

示例 1：
输入：grid = [[0,1],[1,0]]
输出：1

示例 2：
输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2

示例 3：
输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1


提示：
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] 为 0 或 1
grid 中恰有两个岛

链接：https://leetcode.cn/problems/shortest-bridge

"""
from collections import deque
from typing import List

if __name__ == '__main__':
    grid = [[0,1],[1,0]]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        official
        广度优先遍历
            1.正常遍历每个顶点, 如果顶点不是1就跳过
            2.如果顶点是1,就访问1周围的顶点, 如果周围还有1就放入队列, 不是1就跳过, 并且把访问过的1设置为-1(防止重复访问)
                周围 for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1)
                该步的目的是找到两个岛中的其中一个岛, 把一个岛存入 is_land 变量
            3.遍历找到的岛, 把遍历的岛进行 广度优先遍历,找到step
                若广度找到的是 0 就是要建的桥
                若广度找到的是-1 就是之前访问过的岛
                若逛到找到的是 1 就是要返回的step
        """
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                island = []
                grid[i][j] = -1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    island.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            q.append((nx, ny))

                step = 0
                q = island
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1
