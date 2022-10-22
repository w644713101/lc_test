"""
给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。
示例 1：
输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。


示例 2：
输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。


示例 3：
输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成

https://leetcode.cn/problems/distinct-subsequences-ii/
"""
import math
import itertools as it

if __name__ == '__main__':
    s = 'abac'
    res_set = set()
    pass








"""一般困难不能用暴力"""
# if __name__ == '__main__':
#     remainder = math.pow(10, 9)
#     s = "abc"
#     alpha_dict = {}
#     alpha_str = ''
#     for index, value in enumerate(s):
#         if value not in alpha_dict.keys():
#             alpha_dict[value] = [index, ]
#             alpha_str += value
#         else:
#             alpha_dict[value].append(index)
#     alpha_sum = len(alpha_dict.keys())
#     res_num = 0
#     test = []
#     test2 = []
#     for rep_num in range(1, alpha_sum+1):
#         for i in it.product(alpha_str, repeat=rep_num):
#             is_sum = False
#             test2.append(i)
#             for index, value in enumerate(i):
#                 alread_append = []
#                 if index != len(i)-1:
#                     before_list = alpha_dict[value]
#                     before_list = [i for i in before_list if i not in alread_append]
#                     after_list = alpha_dict[i[index+1]]
#                     after_list = [i for i in after_list if i not in alread_append]
#                     before_repeat = []
#                     after_repeat = []
#                     for before_index, before_value in enumerate(before_list):
#                         if value == i[index+1]:
#                             after_repeat.append(before_index)
#                         for after_index, after_value in enumerate(after_list):
#                             if before_value < after_value and before_index not in before_repeat and after_index not in after_repeat:
#                                 is_sum = True
#                                 before_repeat.append(before_index)
#                                 after_repeat.append(after_index)
#                                 alread_append.append(before_index)
#                                 break
#                             else:
#                                 is_sum = False
#                 elif index == 0 and len(i) == 1:
#                     is_sum = True
#                 elif index == len(i)-1 and index != 0:
#                     pass
#                 else:
#                     is_sum = False
#             if is_sum:
#                 test.append(i)
#                 res_num += 1
#     res_num = res_num+1 if len(alpha_str) != len(s) else res_num
#     print(res_num)
#     print(test)
#     print(test2)
#     import pdb;pdb.set_trace()




