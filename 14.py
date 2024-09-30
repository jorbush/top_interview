"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

def get_common_prefix(str_1, str_2, index):
    if index >= len(str_1) or index >= len(str_2):
        return str_1[:index]
    if str_1[index] == str_2[index]:
        return get_common_prefix(str_1, str_2, index + 1)
    else:
        return str_1[:index]

def longest_common_prefix(strs, common_prefix):
    if len(strs) == 0:
        return common_prefix
    current_string = strs.pop(0)
    print(current_string)
    common_prefix_current = get_common_prefix(current_string, common_prefix, 0)
    print(common_prefix_current)
    if common_prefix_current != "":
        return longest_common_prefix(strs, common_prefix_current)
    else: return ""


def longestCommonPrefix(strs: List[str]) -> str:
    return longest_common_prefix(strs, strs[0])

if __name__ == "__main__":
    longestCommonPrefix(["flower","flow","flight"])
    longestCommonPrefix(["dog","racecar","car"])
    longestCommonPrefix(["acc","aaa","aaba"])