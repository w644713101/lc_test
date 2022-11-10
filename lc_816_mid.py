"""
我们有一些二维坐标，如"(1, 3)"或"(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。
此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。


示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

示例 2:
输入: "(00011)"
输出: ["(0.001, 1)", "(0, 0.011)"]
解释: 
0.0, 00, 0001 或 00.01 是不被允许的。

示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

示例 4:
输入: "(100)"
输出: [(10, 0)]
解释: 
1.0 是不被允许的。

提示:
    4 <= S.length <= 12.
    S[0] = "(", S[S.length - 1] = ")", 且字符串S中的其他元素都是数字。

链接：https://leetcode.cn/problems/ambiguous-coordinates
"""
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        """myself, official also O(n3)"""
        res_list = []
        number_string = s[1:-1]
        for i in range(len(number_string)):
            if i == len(number_string)-1:
                continue
            before = number_string[0: i+1]
            before_list = self.get_str2list(before)
            after = number_string[i+1: ]
            after_list = self.get_str2list(after)
            for before_num in before_list:
                for after_num in after_list:
                    res_list.append(f"({before_num}, {after_num})")
        return res_list

    def get_str2list(self, number_str):
        num_list = [number_str, ]
        for i in range(len(number_str)):
            if i == len(number_str)-1 and len(number_str) == 1:
                num_list.append(number_str)
                break
            elif i == len(number_str)-1:
                continue
            else:
                num_list.append(number_str[0: i+1] + "." + number_str[i+1: ])
        return set(list(filter(self.check_number, num_list)))

    def check_number(self, s):
        find_res = s.find('.')
        if find_res == -1 and len(s) != len(str(int(s))):  # 整数,但是是 023,不符合规则
            # print(f'return False s is {s}')
            return False
        elif find_res == -1:  # 整数
            # print(f'return True s is {s}')
            return True
        elif s.endswith('0'):  # 小数
            # print(f'return False s is {s}')
            return False
        elif find_res > 1 and s.startswith('0'):
            return False
        else:
            # print(f'return True s is {s}')
            return True
        # else:
            # print(f'into else return False s is {s}')
            # return False


if __name__ == '__main__':
    t = Solution()
    s_list = ["(100)", "(0123)", "(123)", '(00011)']
    for s in s_list:
        print(t.ambiguousCoordinates(s))
