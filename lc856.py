
"""
给定一个平衡括号字符串S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得A + B分，其中 A 和 B 是平衡括号字符串。
(A) 得2 * A分，其中 A 是平衡括号字符串。


示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例3：

输入： "()()"
输出： 2
示例4：

输入： "(()(()))"
输出： 6


提示：

S是平衡括号字符串，且只含有(和)。
2 <= S.length <= 50


链接：https://leetcode.cn/problems/score-of-parentheses

"""

if __name__ == '__main__':
    test = '(()(()))'
    stack1 = []
    before = None
    after = None
    res = 1
    for value in test:
        if value == '(':
            stack1.append(value)
        if value == ')':
            if len(stack1) == 1:
                before = after
            else:
                after = stack1.pop()
                before = stack1[-1]

            if before == '(':
                res = 2*res
            else:
                res += 1
    import pdb;pdb.set_trace()






